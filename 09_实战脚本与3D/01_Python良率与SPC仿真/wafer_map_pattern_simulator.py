"""CP Wafer Map Spatial Defect Pattern Simulator & Diagnostic Analyzer.

Generates synthetic 300mm-style grid wafer maps showing classic Fab failure
signatures (Edge Ring, Center Bullseye, Scratch Arc, and Reticle Shot Repeater),
prints ASCII wafer maps, and computes yield & edge/center clustering diagnostics.
Uses only Python standard library modules.
"""

from __future__ import annotations

import math
import random
from dataclasses import dataclass


@dataclass
class WaferMap:
    """Grid representation of a wafer map: '.'=pass, 'X'=fail, ' '=outside."""

    name: str
    radius: int
    grid: list[list[str]]

    def stats(self) -> tuple[int, int, float, float, float]:
        """Return (total_dies, fail_dies, yield_pct, center_fail_pct, edge_fail_pct)."""
        total = 0
        fail = 0
        center_tot, center_fail = 0, 0
        edge_tot, edge_fail = 0, 0
        r_edge = self.radius * 0.78

        for y, row in enumerate(self.grid):
            for x, ch in enumerate(row):
                if ch == " ":
                    continue
                dx = x - self.radius
                dy = y - self.radius
                dist = math.hypot(dx, dy)
                total += 1
                is_fail = ch == "X"
                if is_fail:
                    fail += 1
                if dist <= self.radius * 0.45:
                    center_tot += 1
                    if is_fail:
                        center_fail += 1
                elif dist >= r_edge:
                    edge_tot += 1
                    if is_fail:
                        edge_fail += 1

        y_pct = ((total - fail) / total * 100.0) if total else 0.0
        c_pct = (center_fail / center_tot * 100.0) if center_tot else 0.0
        e_pct = (edge_fail / edge_tot * 100.0) if edge_tot else 0.0
        return total, fail, y_pct, c_pct, e_pct

    def render_ascii(self) -> str:
        return "\n".join("".join(row) for row in self.grid)


def build_wafer_map(name: str, pattern: str, radius: int = 10, seed: int = 42) -> WaferMap:
    """Create a synthetic wafer map matching a standard fab defect signature."""
    rng = random.Random(seed)
    size = 2 * radius + 1
    grid = [[" " for _ in range(size)] for _ in range(size)]

    for y in range(size):
        for x in range(size):
            dx = x - radius
            dy = y - radius
            dist = math.hypot(dx, dy)
            if dist > radius + 0.25:
                continue

            fail = rng.random() < 0.02  # 2% baseline random defectivity
            if pattern == "edge_ring" and dist >= radius * 0.78:
                fail = fail or (rng.random() < 0.72)
            elif pattern == "center_bullseye" and dist <= radius * 0.42:
                fail = fail or (rng.random() < 0.78)
            elif pattern == "scratch":
                # Curved CMP scratch arc across upper-right quadrant
                arc_dist = abs(math.hypot(dx - 6, dy + 4) - 6.5)
                if arc_dist < 0.85 and dx >= -1 and dy <= 4:
                    fail = True
            elif pattern == "reticle_repeater":
                # 3x3 reticle shot field; specific sub-die (1, 1) fails in every shot
                if (x % 3 == 1) and (y % 3 == 1):
                    fail = True

            grid[y][x] = "X" if fail else "."

    return WaferMap(name=name, radius=radius, grid=grid)


def diagnose_signature(center_fail_pct: float, edge_fail_pct: float, name: str) -> str:
    """Return likely Fab root cause hint from simple spatial heuristics."""
    if edge_fail_pct > center_fail_pct + 30.0:
        return "Suspected Edge Exclusion / CMP Edge / Etch Focus Ring / Spin-Coat Edge Bead"
    if center_fail_pct > edge_fail_pct + 30.0:
        return "Suspected Showerhead Center Gas Flow / ESC Center Zone Temp / Center CMP Pressure"
    if "Reticle" in name:
        return "Periodic Grid Failure -> Check Photomask / Reticle Pellicle Defect Immediately!"
    return "Localized Linear / Arc Scratch -> Inspect CMP Pad/Slurry Filtration & EFEM Handling"


def main() -> None:
    cases = [
        ("Case 1: Edge Ring (边缘环状失效)", "edge_ring"),
        ("Case 2: Center Bullseye (中心靶心失效)", "center_bullseye"),
        ("Case 3: CMP Scratch Arc (抛光弧形划伤)", "scratch"),
        ("Case 4: Reticle Shot Repeater (光罩周期重复死点)", "reticle_repeater"),
    ]
    for title, pat in cases:
        wm = build_wafer_map(title, pat, radius=9)
        total, fail, y_pct, c_pct, e_pct = wm.stats()
        hint = diagnose_signature(c_pct, e_pct, title)
        print(f"\n=== {title} ===")
        print(wm.render_ascii())
        print(
            f"Dies={total} | Fail={fail} | Yield={y_pct:.1f}% | "
            f"CenterFail={c_pct:.1f}% | EdgeFail={e_pct:.1f}%"
        )
        print(f"Diagnosis Hint: {hint}")


if __name__ == "__main__":
    main()
