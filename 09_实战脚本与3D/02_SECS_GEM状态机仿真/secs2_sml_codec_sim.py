"""SECS-II / HSMS SML Message Encoder, Parser & EAP-Equipment Transaction Simulator.

Demonstrates SEMI E5 (SECS-II) structured item trees (L, A, U4, B) and SML text
representation for standard GEM300 Host (EAP) <-> Equipment communication flows:
- S1F1 / S1F2   : Are You There
- S2F41 / S2F42 : Host Command (PP-SELECT / START)
- S6F11 / S6F12 : Event Report (SlotMapVerified / ProcessCompleted)
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class SecsItem:
    """Represents one node in a SEMI E5 SECS-II data tree."""

    fmt: str  # 'L' (List), 'A' (ASCII), 'U4' (32-bit unsigned), 'B' (Binary)
    value: Any

    def to_sml(self, indent: int = 0) -> str:
        pad = "  " * indent
        if self.fmt == "L":
            items: list[SecsItem] = self.value
            if not items:
                return f"{pad}<L [0]>"
            children = "\n".join(child.to_sml(indent + 1) for child in items)
            return f"{pad}<L [{len(items)}]\n{children}\n{pad}>"
        if self.fmt == "A":
            return f'{pad}<A "{self.value}">'
        if self.fmt == "B":
            hex_val = " ".join(f"0x{b:02X}" for b in self.value)
            return f"{pad}<B [{len(self.value)}] {hex_val}>"
        if self.fmt == "U4":
            return f"{pad}<U4 {self.value}>"
        return f"{pad}<{self.fmt} {self.value}>"


@dataclass(frozen=True)
class SecsMessage:
    stream: int
    function: int
    w_bit: bool
    body: SecsItem | None = None

    @property
    def sf_code(self) -> str:
        return f"S{self.stream}F{self.function}"

    def format_sml(self) -> str:
        w_flag = " W" if self.w_bit else ""
        if self.body is None:
            return f"{self.sf_code}{w_flag}."
        return f"{self.sf_code}{w_flag}\n{self.body.to_sml(1)}."


def build_pp_select_msg(port_id: int, recipe_id: str) -> SecsMessage:
    """Construct S2F41 Host Command for PP-SELECT."""
    body = SecsItem(
        "L",
        [
            SecsItem("A", "PP-SELECT"),
            SecsItem(
                "L",
                [
                    SecsItem("L", [SecsItem("A", "PORTID"), SecsItem("U4", port_id)]),
                    SecsItem("L", [SecsItem("A", "PPID"), SecsItem("A", recipe_id)]),
                ],
            ),
        ],
    )
    return SecsMessage(stream=2, function=41, w_bit=True, body=body)


def build_event_report_msg(data_id: int, ceid: int, lot_id: str, slot_map: str) -> SecsMessage:
    """Construct S6F11 Event Report Send (e.g. SlotMapVerified)."""
    body = SecsItem(
        "L",
        [
            SecsItem("U4", data_id),
            SecsItem("U4", ceid),
            SecsItem(
                "L",
                [
                    SecsItem(
                        "L",
                        [
                            SecsItem("U4", 101),  # RPTID 101
                            SecsItem("L", [SecsItem("A", lot_id), SecsItem("A", slot_map)]),
                        ],
                    )
                ],
            ),
        ],
    )
    return SecsMessage(stream=6, function=11, w_bit=True, body=body)


def main() -> None:
    print("=== SECS-II / HSMS Host (EAP) <-> Equipment Dialogue Simulation ===\n")

    s1f1 = SecsMessage(1, 1, True, None)
    s1f2 = SecsMessage(1, 2, False, SecsItem("L", [SecsItem("A", "LAM-ETCH-03"), SecsItem("A", "v4.12")]))
    print("[EAP -> EQP] Heartbeat Check:")
    print(s1f1.format_sml())
    print("\n[EQP -> EAP] Online Response:")
    print(s1f2.format_sml())

    s2f41 = build_pp_select_msg(port_id=1, recipe_id="28HKMG_GATE_POLY_ETCH_R04")
    s2f42 = SecsMessage(2, 42, False, SecsItem("L", [SecsItem("B", [0x00]), SecsItem("L", [])]))
    print("\n[EAP -> EQP] Remote Recipe Select (PP-SELECT):")
    print(s2f41.format_sml())
    print("\n[EQP -> EAP] Host Command Ack (HCACK=0x00 OK):")
    print(s2f42.format_sml())

    s6f11 = build_event_report_msg(
        data_id=8821,
        ceid=4020,  # CarrierSlotMapVerified
        lot_id="LOT-N28-A9042",
        slot_map="2222222222222222222222221",  # 24 wafers present ('2'), slot 25 empty ('1')
    )
    s6f12 = SecsMessage(6, 12, False, SecsItem("B", [0x00]))
    print("\n[EQP -> EAP] GEM300 E87 SlotMap Event Report:")
    print(s6f11.format_sml())
    print("\n[EAP -> EQP] Event Report Ack (ACKC6=0x00 Accepted):")
    print(s6f12.format_sml())


if __name__ == "__main__":
    main()
