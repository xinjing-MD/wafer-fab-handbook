"""300mm Wafer Gross Die per Wafer (DPW) and Yield Model Calculator.

Computes exact geometric die count on a circular wafer (with edge exclusion)
and compares Poisson, Murphy, Seeds, and Negative Binomial yield models.
Uses only Python standard library modules.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class WaferSpec:
    """Geometric parameters for a semiconductor wafer (in mm)."""

    diameter_mm: float = 300.0
    edge_exclusion_mm: float = 3.0

    @property
    def usable_radius_mm(self) -> float:
        return (self.diameter_mm / 2.0) - self.edge_exclusion_mm


def count_gross_dies(
    die_width_mm: float,
    die_height_mm: float,
    scribe_lane_mm: float = 0.08,
    wafer: WaferSpec = WaferSpec(),
) -> int:
    """Count complete rectangular dies fitting inside the usable wafer circle.

    Uses a centered grid scan checking all four corners of each die pitch cell.
    """
    if die_width_mm <= 0 or die_height_mm <= 0:
        raise ValueError("Die dimensions must be positive.")

    pitch_x = die_width_mm + scribe_lane_mm
    pitch_y = die_height_mm + scribe_lane_mm
    r_sq = wafer.usable_radius_mm**2

    max_cols = int(math.ceil(wafer.usable_radius_mm / pitch_x)) + 1
    max_rows = int(math.ceil(wafer.usable_radius_mm / pitch_y)) + 1

    good_count = 0
    for row in range(-max_rows, max_rows + 1):
        y0 = row * pitch_y
        y1 = y0 + die_height_mm
        for col in range(-max_cols, max_cols + 1):
            x0 = col * pitch_x
            x1 = x0 + die_width_mm
            corners = ((x0, y0), (x1, y0), (x0, y1), (x1, y1))
            if all((cx * cx + cy * cy) <= r_sq for cx, cy in corners):
                good_count += 1
    return good_count


def calculate_yield_models(
    die_area_cm2: float,
    defect_density_per_cm2: float,
    cluster_alpha: float = 2.0,
) -> dict[str, float]:
    """Return predicted die yields (0.0 - 1.0) across four standard fab models."""
    if die_area_cm2 <= 0 or defect_density_per_cm2 < 0 or cluster_alpha <= 0:
        raise ValueError("Area and alpha must be positive; D0 must be non-negative.")

    da = defect_density_per_cm2 * die_area_cm2
    if da == 0.0:
        return {"Poisson": 1.0, "Murphy": 1.0, "Seeds": 1.0, "NegativeBinomial": 1.0}

    poisson = math.exp(-da)
    murphy = ((1.0 - math.exp(-da)) / da) ** 2
    seeds = 1.0 / (1.0 + da)
    neg_binom = (1.0 + da / cluster_alpha) ** (-cluster_alpha)
    return {
        "Poisson": poisson,
        "Murphy": murphy,
        "Seeds": seeds,
        "NegativeBinomial": neg_binom,
    }


def main() -> None:
    wafer = WaferSpec(diameter_mm=300.0, edge_exclusion_mm=3.0)
    scenarios = [
        ("Small MCU Die (4 x 4 mm)", 4.0, 4.0, 0.08),
        ("Mobile SoC Die (10 x 12 mm)", 10.0, 12.0, 0.08),
        ("Large AI GPU Die (26 x 30 mm)", 26.0, 30.0, 0.08),
    ]
    d0 = 0.08  # defects / cm^2
    alpha = 2.0

    print(f"=== 300mm Wafer Yield Simulation (D0={d0}/cm^2, alpha={alpha}) ===")
    for name, w_mm, h_mm, scribe in scenarios:
        dpw = count_gross_dies(w_mm, h_mm, scribe, wafer)
        area_cm2 = (w_mm * h_mm) / 100.0
        yields = calculate_yield_models(area_cm2, d0, alpha)

        print(f"\n[{name}] Area={area_cm2:.2f} cm^2 | Gross DPW={dpw}")
        for model_name, y in yields.items():
            good_dies = int(round(dpw * y))
            print(f"  - {model_name:17s}: {y * 100:6.2f}%  (~{good_dies} good dies/wafer)")


if __name__ == "__main__":
    main()
