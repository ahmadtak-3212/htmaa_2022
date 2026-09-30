# Week 4: topology-optimized pencil cup

The assignment was to make something that can't be made subtractively. I made a pencil cup whose shape came from **SolidWorks topology optimization** and printed it in black PLA.

![Printed cup](../docs/images/week04/result_print.jpg)

Full write-up: [week04_3d_printing.md](../docs/writeups/week04_3d_printing.md)

## Files

| Path | What |
|---|---|
| `mechanical/cad/cup_v1/Pencil_Cup.SLDPRT` | Base design with the topology study |
| `mechanical/cad/cup_v1/Pencil_Cup-Topology Study 1/` | SolidWorks Simulation study files (loads, mesh, results) |
| `mechanical/cad/cup_v1/Ahmad/` | The resulting mesh (`.stl`, `.ply`) and screenshots |
| `mechanical/exports/3mf/Pencil_Cup-Topology Study 1_Smooth.3mf` | Smoothed mesh, ready to slice |
| `mechanical/cad/cup_v2/`, `cup_v3/` | Later iterations, including a mesh split into bodies and a cup with a cap |

## Rebuild

1. **Topology study** (SolidWorks Simulation): fix the bottom face; apply **1 MPa** pressure on the top faces and **1 N·m** torque on the top ring; set the goal to minimize mass while keeping stiffness. It took about 40 minutes to solve.
2. Export the smoothed mesh, or use the `.3mf` here.
3. **Print:** Ultimaker S5, black PLA, **0.6 mm nozzle, 0.2 mm layers**. The print took about 16 h.

## Results

The print came out clean, with the organic, non-machinable shape the assignment asked for. For the 3D-scanning part of the week, a scan of a coffee cup produced a mesh of about 1.85 M faces. Mesh cleanup in MeshLab crashed, so that scan wasn't printed.

_Formerly `pencil_cup_project`. Part of [htmaa_2022](../README.md), MIT How to Make (Almost) Anything, fall 2022._
