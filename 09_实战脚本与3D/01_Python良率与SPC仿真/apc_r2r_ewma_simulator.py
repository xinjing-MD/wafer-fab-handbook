"""Fab Run-to-Run (R2R) Double-EWMA Advanced Process Control (APC) Simulator.

Simulates an Etch/CMP process experiencing gradual linear chamber drift
plus a sudden preventive maintenance (PM) step disturbance at Lot #25.
Compares Open-Loop (no APC) vs Closed-Loop Double-EWMA APC on CD/Thickness control.
"""

from __future__ import annotations

import math
import random
import statistics


def simulate_r2r_control(
    num_lots: int = 45,
    target_nm: float = 20.0,
    drift_per_lot: float = 0.04,
    pm_step_lot: int = 25,
    pm_step_shift: float = -1.20,
    w1: float = 0.35,
    w2: float = 0.20,
    seed: int = 7,
) -> None:
    rng = random.Random(seed)
    open_loop_errs: list[float] = []
    apc_errs: list[float] = []

    # Plant state: y_t = u_t (recipe setpoint offset) + true_bias_t + noise
    # Initial true chamber bias = 0.0 nm; recipe gain = 1.0 nm / unit
    u_apc = target_nm
    est_intercept = 0.0
    est_drift = 0.0
    cumulative_drift = 0.0

    print("=== Run-to-Run (R2R) Double-EWMA APC vs Open-Loop Simulation ===")
    print(f"Target={target_nm:.1f}nm | Chamber Drift=+{drift_per_lot:.2f}nm/lot | PM Step at Lot#{pm_step_lot} ({pm_step_shift:+.2f}nm)")
    print(f"{'Lot#':>4s} | {'TrueBias':>8s} | {'OpenLoop':>8s} | {'APC_Out':>8s} | {'APC_Recipe':>10s}")
    print("-" * 52)

    for lot in range(1, num_lots + 1):
        if lot == pm_step_lot:
            cumulative_drift += pm_step_shift
        else:
            cumulative_drift += drift_per_lot

        noise = rng.gauss(0.0, 0.08)
        y_open = target_nm + cumulative_drift + noise
        y_apc = u_apc + cumulative_drift + noise

        open_loop_errs.append(y_open - target_nm)
        apc_errs.append(y_apc - target_nm)

        # Standard Double-EWMA (Butler & Stefani) intercept + ramp drift tracker
        residual = y_apc - u_apc
        prev_intercept = est_intercept
        est_intercept = w1 * residual + (1.0 - w1) * (prev_intercept + est_drift)
        if lot > 1:
            est_drift = w2 * (residual - prev_intercept) + (1.0 - w2) * est_drift

        # Compute next lot recipe setpoint
        u_next = target_nm - (est_intercept + est_drift)

        if lot <= 5 or abs(lot - pm_step_lot) <= 2 or lot == num_lots:
            print(f"{lot:4d} | {cumulative_drift:+8.3f} | {y_open:8.3f} | {y_apc:8.3f} | {u_apc:10.3f}")

        u_apc = u_next

    rmse_open = math.sqrt(sum(e * e for e in open_loop_errs) / len(open_loop_errs))
    rmse_apc = math.sqrt(sum(e * e for e in apc_errs) / len(apc_errs))
    print("\n=== Performance Summary (45 Lots) ===")
    print(f"Open-Loop (No APC)   RMSE: {rmse_open:.3f} nm | Max |Error|: {max(abs(e) for e in open_loop_errs):.3f} nm")
    print(f"Double-EWMA APC      RMSE: {rmse_apc:.3f} nm | Max |Error|: {max(abs(e) for e in apc_errs):.3f} nm")
    print(f"Variance Reduction Ratio  : {(1.0 - rmse_apc / rmse_open) * 100:.1f}%")


if __name__ == "__main__":
    simulate_r2r_control()
