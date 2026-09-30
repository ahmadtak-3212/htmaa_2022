# Week 2: parametric living-hinge box

This week I built a **parametric living-hinge part** in SolidWorks and used it to laser-cut a cup-shaped box with a base, a hinged wall and a cover. I also vinyl-cut my mom's name in Arabic calligraphy.

![Living-hinge box](../docs/images/week02/living-hinge.jpg)

Full write-up: [week02_laser_and_vinyl_cutting.md](../docs/writeups/week02_laser_and_vinyl_cutting.md)

## Files

| Path | What |
|---|---|
| `mechanical/cad/Wall.SLDPRT` | The parametric living-hinge wall. Change a few dimensions and it regenerates: hinge size, slot spacing (which sets stiffness), finger-joint chamfer and material thickness. |
| `mechanical/cad/Base.SLDPRT`, `Cover.SLDPRT` | Base with finger joints; the cover is the base with a hole through it |
| `mechanical/exports/dxf/*.DXF` | Flat cut files for the laser |

## Rebuild

1. Open `Wall.SLDPRT` in SolidWorks. Set the material thickness and your laser's kerf, then adjust the hinge length and spacing.
2. Export each part's face as DXF, or use the DXFs here, and cut them on a laser cutter.
3. The group characterization found that cardboard cuts at **75 % power / 10 % speed** on our laser, with a kerf of about **1.14 mm**. Recalibrate for your machine and material.

## Results

The finished cup is photographed above. The write-up covers the process, including the vinyl-cut calligraphy.

_Formerly `ivan_project`. Part of [htmaa_2022](../README.md), MIT How to Make (Almost) Anything, fall 2022._
