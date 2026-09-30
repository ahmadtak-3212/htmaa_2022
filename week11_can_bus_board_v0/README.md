# Week 11: SAMD21 CAN board, early version

The first layout of the week 11 CAN board: an ATSAMD21E18A, AP1117-5.0 and NCP1117-3.3 regulators, a power switch, a 10-pin SWD header, and a 7-pin socket for an MCP2515 module, on a 40 × 45 mm board. It was superseded by the sender and receiver pair in [`../week11_12_can_bus_link`](../week11_12_can_bus_link), which is the version that was built and tested.

Full write-up: [week11_networking.md](../docs/writeups/week11_networking.md)

## Files

| Path | What |
|---|---|
| `electrical/can_board/Can_Project.kicad_pro` | KiCad 6 project (schematic + PCB). No Gerbers were exported. |
| `electrical/can_board/samd21.pretty/` | SAMD21E (TQFP-32) footprint |

_Formerly `can_project`. Part of [htmaa_2022](../README.md), MIT How to Make (Almost) Anything, fall 2022._
