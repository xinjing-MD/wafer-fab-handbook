"""Fab Operating Curve Simulator (Kingman Queueing Formula & Little's Law).

Demonstrates why wafer fab cycle time (X-factor) rises exponentially as
bottleneck tool (e.g., EUV/ArFi Lithography) utilization exceeds 85-90%,
and why reducing variability (unscheduled downtime / batching) shifts the curve down.
"""

from __future__ import annotations


def kingman_wait_time_hours(
    utilization: float,
    mean_proc_hours: float,
    ca_sq: float,
    ce_sq: float,
    servers: int = 1,
) -> float:
    """Compute approximate steady-state waiting time Wq via Kingman's G/G/m equation."""
    if not (0.0 < utilization < 1.0):
        raise ValueError("Utilization must be strictly between 0 and 1.")
    variability = (ca_sq + ce_sq) / 2.0
    rho_exp = utilization ** (2.0 * (servers + 1.0) ** 0.5 - 1.0)
    congestion = rho_exp / (servers * (1.0 - utilization))
    return variability * congestion * mean_proc_hours


def main() -> None:
    raw_pt_days = 18.0  # Theoretical raw processing time (zero wait) across 1,000 steps
    num_bottleneck_visits = 60  # Litho re-entrant visits per lot
    litho_proc_hr = 0.60  # 36 minutes per FOUP lot at scanner
    scanners = 4  # 4 parallel EUV/ArFi scanners in bay

    print("=== Wafer Fab Operating Curve (4 Parallel Bottleneck Scanners) ===")
    print(f"Raw Process Time (RPT) = {raw_pt_days:.1f} days | Litho Visits = {num_bottleneck_visits}\n")

    # Compare High-Variability Fab (unplanned downs / hot lots) vs Lean Fab
    print(f"{'Utilization':>11s} | {'High-Var X-Fac':>14s} | {'High-Var CT(d)':>14s} | {'Lean X-Fac':>10s} | {'Lean CT(d)':>10s}")
    print("-" * 72)

    for u_pct in [50, 65, 75, 80, 85, 90, 93, 96]:
        u = u_pct / 100.0
        # High variability: Ca^2=1.2, Ce^2=1.8 (frequent PMs/downs/hot lots)
        wq_high = kingman_wait_time_hours(u, litho_proc_hr, ca_sq=1.2, ce_sq=1.8, servers=scanners)
        # Lean fab: Ca^2=0.5, Ce^2=0.6 (stable equipment, smooth dispatching)
        wq_lean = kingman_wait_time_hours(u, litho_proc_hr, ca_sq=0.5, ce_sq=0.6, servers=scanners)

        # Total bottleneck + proportional downstream queue delay proxy
        ct_high = raw_pt_days + (wq_high * num_bottleneck_visits * 2.2) / 24.0
        ct_lean = raw_pt_days + (wq_lean * num_bottleneck_visits * 2.2) / 24.0

        print(
            f"{u_pct:10d}% | {ct_high / raw_pt_days:13.2f}x | {ct_high:13.1f}d | "
            f"{ct_lean / raw_pt_days:9.2f}x | {ct_lean:9.1f}d"
        )

    print("\nLittle's Law Insight: WIP = Throughput * CycleTime.")
    print("At 93%+ bottleneck utilization, pushing 3% more wafer starts causes WIP and Cycle Time to skyrocket!")


if __name__ == "__main__":
    main()
