# htmaa_2022: MIT How to Make (Almost) Anything, fall 2022

Weekly assignments from MIT's How to Make (Almost) Anything (Sept 7 – Dec 14, 2022), one folder per assignment. The final project, **Oliya**, a full-size electric ATV built with Raiphy, has its own project: [`oliya_project`](../oliya_project). Weeks 7–10 (the ATV's dashboard audio system), week 8 (the ATV emblem) and week 14 (the welded ATV hood) went straight into Oliya, so they live there.

The full write-up for every week is in [`docs/writeups/`](docs/writeups), with the original photos and videos in `docs/images/`. They were converted from my class documentation pages (kept in `menya_project/archive/menya_how_to_make`).

| Week | Assignment | Folder | Write-up |
|---|---|---|---|
| 1 | 3D design (final-project concept) | — | [week01](docs/writeups/week01_3d_design.md) |
| 2 | Laser and vinyl cutting | [`week02_living_hinge_box`](week02_living_hinge_box) | [week02](docs/writeups/week02_laser_and_vinyl_cutting.md) |
| 3 | Electronics production: SAMD11C CMSIS-DAP programmer | [`week03_d11c_programmer`](week03_d11c_programmer) | [week03](docs/writeups/week03_electronics_production.md) |
| 4 | 3D printing: topology-optimized pencil cup | [`week04_topology_cup`](week04_topology_cup) | [week04](docs/writeups/week04_3d_printing.md) |
| 5 | Electronics design: ATtiny1614 OLED board (ATV dashboard display) | [`week05_oled_display_board`](week05_oled_display_board) | [week05](docs/writeups/week05_electronics_design.md) |
| 6 | Computer-controlled machining: plywood chest | [`week06_plywood_chest`](week06_plywood_chest) | [week06](docs/writeups/week06_computer_controlled_machining.md) |
| 7 | Embedded programming: spectrum analyzer / audio amp | in `oliya_project` | [week07](docs/writeups/week07_embedded_programming.md) |
| 8 | Molding and casting: ATV emblem | in `oliya_project` | [week08](docs/writeups/week08_molding_and_casting.md) |
| 9 | Input devices: audio mixer / waveform display | in `oliya_project` | [week09](docs/writeups/week09_input_devices.md) |
| 10 | Output devices: bridged LM386 amplifier | in `oliya_project` | [week10](docs/writeups/week10_output_devices.md) |
| 11 | Networking: CAN bus sender/receiver | [`week11_12_can_bus_link`](week11_12_can_bus_link), [`week11_can_bus_board_v0`](week11_can_bus_board_v0) | [week11](docs/writeups/week11_networking.md) |
| 12 | Interface programming: Kivy CAN logger | [`week11_12_can_bus_link`](week11_12_can_bus_link) | [week12](docs/writeups/week12_interface_programming.md) |
| 13 | Machine building: group drawing machine | [`week13_drawing_machine`](week13_drawing_machine) | [week13](docs/writeups/week13_machine_building.md) |
| 14 | Wildcard: sheet metal and welding (ATV hood) | in `oliya_project` | [week14](docs/writeups/week14_wildcard_welding.md) |

**Week 13 was a group project.** My part: organizing the group and setting up the team GitHub repo, machining the aluminum-extrusion frame (cutting 2060 extrusion to size and turning a 2060 into a 2020 for the x-axis), sourcing the base, printing corner brackets, and designing the limit-switch PCB (`week13_drawing_machine/electrical/limit_switch`). `week13_drawing_machine` is its own git repo (the team's `HTM_Drawing_Bot`) and is left as the team made it.

![Week 3 programmer](docs/images/week03/result.jpg)
![Week 6 chest](docs/images/week06/final.jpg)

See [docs/STRUCTURE.md](docs/STRUCTURE.md) for the layout conventions.
