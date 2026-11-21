"""Semiconductor Fab Unit Process Physics Simulator.

Includes three core engineering models (pure Python standard library):
1. Deal-Grove Thermal Oxidation Kinetics (dry vs wet O2 across 900-1100 C)
2. Rayleigh Lithography Resolution (CD) and Depth of Focus (DOF) comparison
3. LSS Gaussian Ion Implantation Dopant Depth Profile N(x)
"""

from __future__ import annotations

import math


def deal_grove_thickness_um(time_hours: float, a_um: float, b_um2_hr: float, x_initial_um: float = 0.0) -> float:
    """Solve x_o^2 + A * x_o = B * (t + tau) for oxide thickness x_o in micrometers."""
    if time_hours < 0 or b_um2_hr <= 0:
        raise ValueError("Time must be non-negative and B must be positive.")
    tau = (x_initial_um**2 + a_um * x_initial_um) / b_um2_hr
    disc = a_um**2 + 4.0 * b_um2_hr * (time_hours + tau)
    return 0.5 * (-a_um + math.sqrt(disc))


def run_deal_grove_demo() -> None:
    print("=== 1. Deal-Grove Thermal Oxidation (<100> Si, x_i = 0) ===")
    # Classic empirical parameters for <100> silicon oxidation
    regimes = [
        ("Dry O2 @ 900 C", 0.30, 0.005),
        ("Dry O2 @ 1000 C", 0.165, 0.0117),
        ("Wet H2O @ 1000 C", 0.305, 0.387),
        ("Wet H2O @ 1100 C", 0.110, 0.510),
    ]
    times_min = [10, 30, 60, 120]
    header = f"{'Condition':20s} | " + " | ".join(f"{t:4d} min" for t in times_min)
    print(header)
    print("-" * len(header))
    for name, a_um, b_val in regimes:
        vals = [deal_grove_thickness_um(t / 60.0, a_um, b_val) * 1000.0 for t in times_min]
        row = f"{name:20s} | " + " | ".join(f"{v:6.1f}nm" for v in vals)
        print(row)


def run_litho_window_demo() -> None:
    print("\n=== 2. Lithography Rayleigh Scaling (k1=0.30, k2=0.50) ===")
    k1, k2 = 0.30, 0.50
    scanners = [
        ("KrF DUV (Dry)", 248.0, 0.80, 1.00),
        ("ArF DUV (Dry)", 193.0, 0.93, 1.00),
        ("ArFi Immersion (H2O)", 193.0, 1.35, 1.44),
        ("EUV 0.33 NA", 13.5, 0.33, 1.00),
        ("High-NA EUV 0.55 NA", 13.5, 0.55, 1.00),
    ]
    print(f"{'System':22s} | {'Min HP (nm)':>11s} | {'DOF (nm)':>10s}")
    print("-" * 50)
    for name, lam, na, n_med in scanners:
        cd_hp = k1 * lam / na
        dof = k2 * n_med * lam / (na**2)
        print(f"{name:22s} | {cd_hp:11.1f} | {dof:10.1f}")


def gaussian_implant_profile(depth_um: float, dose_cm2: float, rp_um: float, drp_um: float) -> float:
    """Compute Gaussian dopant concentration N(x) in atoms/cm^3 at depth_um."""
    drp_cm = drp_um * 1e-4
    peak = dose_cm2 / (math.sqrt(2.0 * math.pi) * drp_cm)
    exponent = -0.5 * ((depth_um - rp_um) / drp_um) ** 2
    return peak * math.exp(exponent)


def run_implant_profile_demo() -> None:
    print("\n=== 3. LSS Gaussian Ion Implantation Profile (Boron, Dose=2e15/cm^2, Rp=0.08um, dRp=0.03um) ===")
    dose, rp, drp = 2.0e15, 0.08, 0.03
    bg_nd = 1.0e16  # N-well background concentration -> marks metallurgical junction Xj
    depths = [0.00, 0.04, 0.08, 0.12, 0.16, 0.20, 0.24]
    xj_um = rp + drp * math.sqrt(2.0 * math.log((dose / (math.sqrt(2.0 * math.pi) * drp * 1e-4)) / bg_nd))
    for d in depths:
        conc = gaussian_implant_profile(d, dose, rp, drp)
        bar = "#" * max(1, int(math.log10(max(conc, 1e12)) - 12) * 3)
        print(f"  x = {d:4.2f} um | N(x) = {conc:9.2e} /cm^3 | {bar}")
    print(f"  Estimated Junction Depth Xj (at N_bg={bg_nd:.1e}/cm^3): {xj_um:.3f} um ({xj_um * 1000:.0f} nm)")


if __name__ == "__main__":
    run_deal_grove_demo()
    run_litho_window_demo()
    run_implant_profile_demo()
