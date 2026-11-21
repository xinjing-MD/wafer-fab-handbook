"""SEMI E10 Equipment State Machine & SEMI E84 OHT Load Port Handshake Simulator.

Helps CIM/MES/EE learners visualize standard fab equipment states and the
8-signal PIO optical handshake between an Overhead Hoist Transport (OHT) and Load Port.
"""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class E10State(str, Enum):
    """Six basic equipment states defined by SEMI E10."""

    PRODUCTIVE = "PRD (Productive)"
    STANDBY = "SBY (Standby)"
    ENGINEERING = "ENG (Engineering)"
    SCHEDULED_DOWNTIME = "SDT (Scheduled Downtime)"
    UNSCHEDULED_DOWNTIME = "UDT (Unscheduled Downtime)"
    NON_SCHEDULED = "NST (Non-Scheduled)"


@dataclass
class E84Signals:
    """8-bit parallel I/O handshake lines between OHT (Active) and Load Port (Passive)."""

    # OHT -> Load Port (Active)
    valid: bool = False
    cs_0: bool = False
    tr_req: bool = False
    busy: bool = False
    compt: bool = False

    # Load Port -> OHT (Passive)
    l_req: bool = False
    u_req: bool = False
    ready: bool = False

    def snapshot(self) -> str:
        oht_bits = f"VALID={int(self.valid)} CS0={int(self.cs_0)} TR_REQ={int(self.tr_req)} BUSY={int(self.busy)} COMPT={int(self.compt)}"
        lp_bits = f"L_REQ={int(self.l_req)} U_REQ={int(self.u_req)} READY={int(self.ready)}"
        return f"OHT[{oht_bits}] | LP[{lp_bits}]"


def simulate_e84_load_sequence(foup_id: str) -> None:
    """Print step-by-step SEMI E84 FOUP load handshake sequence."""
    sig = E84Signals()
    steps = [
        ("1. Idle (Load Port empty, waiting for FOUP)", {}),
        ("2. OHT arrives overhead and asserts VALID + CS_0", {"valid": True, "cs_0": True}),
        ("3. Load Port confirms empty & clamped-off -> asserts L_REQ", {"l_req": True}),
        ("4. OHT requests transfer start -> asserts TR_REQ", {"tr_req": True}),
        ("5. Load Port interlock clear -> asserts READY", {"ready": True}),
        ("6. OHT lowers hoist belts & places FOUP -> asserts BUSY", {"busy": True}),
        ("7. Presence sensor detects FOUP -> Load Port clears L_REQ", {"l_req": False}),
        ("8. OHT retracts gripper & clears BUSY, asserts COMPT", {"busy": False, "compt": True}),
        ("9. Load Port clears READY; OHT clears remaining lines -> Done", {"ready": False, "valid": False, "cs_0": False, "tr_req": False, "compt": False}),
    ]

    print(f"=== SEMI E84 Load Handshake Simulation ({foup_id}) ===")
    for desc, updates in steps:
        for key, val in updates.items():
            setattr(sig, key, val)
        print(f"{desc}\n   {sig.snapshot()}")


def simulate_e10_cycle() -> None:
    """Print a simplified lot run transition across SEMI E10 equipment states."""
    transitions = [
        (E10State.STANDBY, "Waiting for FOUP arrival from OHT"),
        (E10State.PRODUCTIVE, "FOUP clamped, E87 verified, PM1-PM4 processing 25 wafers"),
        (E10State.SCHEDULED_DOWNTIME, "Preventive Maintenance (PM): RF match & ESC check"),
        (E10State.ENGINEERING, "Process Engineer qualification (Qual wafer CD/Particle check)"),
        (E10State.STANDBY, "Tool released to MES production, ready for next lot"),
    ]
    print("\n=== SEMI E10 Equipment State Transitions ===")
    for state, reason in transitions:
        print(f"  -> {state.value:30s} | {reason}")


if __name__ == "__main__":
    simulate_e84_load_sequence("FOUP-300-A012")
    simulate_e10_cycle()
