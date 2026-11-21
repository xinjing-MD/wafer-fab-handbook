"""SPC Process Capability (Cp/Cpk) and Western Electric Rule Checker.

Demonstrates how a Fab SPC system evaluates metrology data (e.g. Gate CD in nm)
and catches drift or out-of-control (OOC) trends before wafers scrap.
Uses only Python standard library modules.
"""

from __future__ import annotations

import math
import statistics
from dataclasses import dataclass


@dataclass(frozen=True)
class CapabilityReport:
    mean: float
    stdev: float
    cp: float
    cpk: float
    ucl: float
    lcl: float


def compute_capability(
    samples: list[float], lsl: float, usl: float
) -> CapabilityReport:
    """Compute sample mean, stdev, Cp, Cpk, and 3-sigma control limits."""
    if len(samples) < 2:
        raise ValueError("Need at least 2 samples.")
    if usl <= lsl:
        raise ValueError("USL must be greater than LSL.")

    mean = statistics.mean(samples)
    stdev = statistics.stdev(samples)
    if stdev == 0:
        raise ValueError("Sample standard deviation is zero.")

    cp = (usl - lsl) / (6.0 * stdev)
    cpu = (usl - mean) / (3.0 * stdev)
    cpl = (mean - lsl) / (3.0 * stdev)
    cpk = min(cpu, cpl)

    return CapabilityReport(
        mean=mean,
        stdev=stdev,
        cp=cp,
        cpk=cpk,
        ucl=mean + 3.0 * stdev,
        lcl=mean - 3.0 * stdev,
    )


def check_western_electric_rules(
    series: list[float], center: float, sigma: float
) -> list[str]:
    """Check core Western Electric SPC rules (Rule 1, Rule 2, Rule 3, Rule 4)."""
    alerts: list[str] = []
    if sigma <= 0:
        return alerts

    # Rule 1: 1 point beyond 3-sigma
    for idx, val in enumerate(series):
        if abs(val - center) > 3.0 * sigma:
            alerts.append(f"Rule 1 (Beyond 3-sigma) at sample #{idx + 1}: {val:.3f}")

    # Rule 2: 9 consecutive points on the same side of centerline
    for start in range(len(series) - 8):
        window = series[start : start + 9]
        if all(v > center for v in window) or all(v < center for v in window):
            alerts.append(
                f"Rule 2 (9 consecutive same-side) ending at sample #{start + 9}"
            )

    # Rule 3: 6 consecutive points strictly increasing or decreasing
    for start in range(len(series) - 5):
        w = series[start : start + 6]
        inc = all(w[i] < w[i + 1] for i in range(5))
        dec = all(w[i] > w[i + 1] for i in range(5))
        if inc or dec:
            trend = "increasing" if inc else "decreasing"
            alerts.append(
                f"Rule 3 (6 consecutive {trend}) ending at sample #{start + 6}"
            )

    # Rule 4: 14 consecutive points alternating up and down (chamber mismatch signature)
    for start in range(len(series) - 13):
        w = series[start : start + 14]
        diffs = [w[i + 1] - w[i] for i in range(13)]
        if all(diffs[i] * diffs[i + 1] < 0 for i in range(12)):
            alerts.append(
                f"Rule 4 (14 alternating points) ending at sample #{start + 14}"
            )

    return alerts


def main() -> None:
    # Target Gate CD = 20.0 nm, Spec = [18.5, 21.5] nm
    lsl, target, usl = 18.5, 20.0, 21.5
    baseline_sigma = 0.25

    # Synthetic wafer CD trend showing gradual drift (etch chamber polymer buildup)
    lot_cds = [
        19.95, 20.05, 19.90, 20.10, 19.98,
        20.02, 20.12, 20.20, 20.28, 20.36,
        20.44, 20.52, 20.82,
    ]

    report = compute_capability(lot_cds, lsl=lsl, usl=usl)
    print("=== Gate CD SPC Report ===")
    print(f"Samples : {len(lot_cds)} | Target: {target:.2f} nm | Spec: [{lsl}, {usl}]")
    print(f"Mean    : {report.mean:.3f} nm | Stdev: {report.stdev:.3f} nm")
    print(f"Cp      : {report.cp:.3f} | Cpk: {report.cpk:.3f}")
    print(f"3-sigma : LCL={report.lcl:.3f}, UCL={report.ucl:.3f}")

    alerts = check_western_electric_rules(lot_cds, center=target, sigma=baseline_sigma)
    print("\n=== Western Electric Rule Alerts (against baseline sigma=0.25) ===")
    if alerts:
        for alert in alerts:
            print(f"  [OOC] {alert}")
    else:
        print("  All points in statistical control.")


if __name__ == "__main__":
    main()
