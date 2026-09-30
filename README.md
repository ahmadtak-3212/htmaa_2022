# htmaa_2022: MIT How to Make (Almost) Anything, fall 2022

My weekly assignments from MIT's **How to Make (Almost) Anything** (MAS.863, Sept 7 – Dec 14, 2022), with one folder per assignment. Each folder has its design files and a README explaining how to rebuild it. The full write-ups, with photos and videos, are in [`docs/writeups/`](docs/writeups).

My final project was **Oliya**, a full-size electric ATV built with Raiphy. It has its own repo: **[oliya_project](https://github.com/ahmadtak-3212/oliya_project)**. Weeks 5 and 7–10 (the ATV's dashboard display and audio system), week 8 (the ATV emblem) and week 14 (the welded hood) fed straight into it, so their design files live there.

| Week 3 programmer | Week 6 chest | Week 11 CAN boards |
|---|---|---|
| ![Week 3](docs/images/week03/result.jpg) | ![Week 6](docs/images/week06/final.jpg) | ![Week 11](docs/images/week11/result-0.jpg) |

## Weeks

| Week | Assignment | What I made | Files | Write-up |
|---|---|---|---|---|
| 1 | 3D design | Oliya ATV concept CAD | [oliya_project](https://github.com/ahmadtak-3212/oliya_project) | [week01](docs/writeups/week01_3d_design.md) |
| 2 | Laser and vinyl cutting | Parametric living-hinge box; vinyl-cut calligraphy | [`week02_living_hinge_box`](week02_living_hinge_box) | [week02](docs/writeups/week02_laser_and_vinyl_cutting.md) |
| 3 | Electronics production | Milled SAMD11C CMSIS-DAP programmer | [`week03_d11c_programmer`](week03_d11c_programmer) | [week03](docs/writeups/week03_electronics_production.md) |
| 4 | 3D printing and scanning | Topology-optimized pencil cup | [`week04_topology_cup`](week04_topology_cup) | [week04](docs/writeups/week04_3d_printing.md) |
| 5 | Electronics design | ATtiny1614 + OLED board (ATV dashboard display) | [`week05_oled_display_board`](week05_oled_display_board) | [week05](docs/writeups/week05_electronics_design.md) |
| 6 | Computer-controlled machining | Parametric CNC-routed plywood chest | [`week06_plywood_chest`](week06_plywood_chest) | [week06](docs/writeups/week06_computer_controlled_machining.md) |
| 7 | Embedded programming | Spectrum analyzer / audio amplifier | [oliya_project](https://github.com/ahmadtak-3212/oliya_project) | [week07](docs/writeups/week07_embedded_programming.md) |
| 8 | Molding and casting | Oliya emblem | [oliya_project](https://github.com/ahmadtak-3212/oliya_project) | [week08](docs/writeups/week08_molding_and_casting.md) |
| 9 | Input devices | Audio mixer and waveform display input | [oliya_project](https://github.com/ahmadtak-3212/oliya_project) | [week09](docs/writeups/week09_input_devices.md) |
| 10 | Output devices | Bridged LM386 speaker amplifier | [oliya_project](https://github.com/ahmadtak-3212/oliya_project) | [week10](docs/writeups/week10_output_devices.md) |
| 11 | Networking | SAMD21 + MCP2515 CAN sender and receiver | [`week11_12_can_bus_link`](week11_12_can_bus_link), [`week11_can_bus_board_v0`](week11_can_bus_board_v0) | [week11](docs/writeups/week11_networking.md) |
| 12 | Interface programming | Kivy CAN logger app | [`week11_12_can_bus_link`](week11_12_can_bus_link) | [week12](docs/writeups/week12_interface_programming.md) |
| 13 | Machine building | Group drawing machine | [HTM_Drawing_Bot](https://github.com/ahmadtak-3212/HTM_Drawing_Bot) (team repo) | [week13](docs/writeups/week13_machine_building.md) |
| 14 | Wildcard | Sheet metal and welding (ATV hood) | [oliya_project](https://github.com/ahmadtak-3212/oliya_project) | [week14](docs/writeups/week14_wildcard_welding.md) |

**Week 13 was a group project** and lives in the team's own repo, [HTM_Drawing_Bot](https://github.com/ahmadtak-3212/HTM_Drawing_Bot). My parts were:
- organizing the group and setting up the team repo;
- machining the aluminum-extrusion frame (cutting 2060 extrusion to size and machining a 2060 down to a 2020 for the x-axis);
- sourcing the base and printing corner brackets;
- designing the limit-switch PCB.

## Tools used

| Kind | Tools |
|---|---|
| CAD | SolidWorks (including Simulation / topology study), Fusion 360 (CAM) |
| Electronics | KiCad 6; boards milled on a Bantam desktop mill |
| Firmware | Arduino IDE with megaTinyCore (ATtiny1614) and a SAMD core (SAMD11/SAMD21); `edbg` for SWD flashing |
| Software | Python 3.9 + Kivy 2.1 + pyserial |
| Fabrication | Laser cutter, vinyl cutter, Ultimaker S5, shop CNC router, water jet, MIG welder |

## Layout

```
htmaa_2022/
├── docs/
│   ├── writeups/        one Markdown write-up per week
│   └── images/weekNN/   photos, videos, downloads referenced by the write-ups
│       └── renders/     PCB renders generated from the Gerbers
└── weekNN_<name>/       design files for that week (each has its own README)
```

The write-ups were converted from my original class documentation pages. See [docs/STRUCTURE.md](docs/STRUCTURE.md) for the folder conventions.
