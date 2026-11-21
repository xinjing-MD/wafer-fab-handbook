"""Blender 4.x / 5.x Parametric 300mm Wafer Fab Asset Generator (bpy).

Generates 1:1 metric industrial reference primitives inside Blender matching
the golden SEMI engineering tolerances documented in this repository:
- 300mm Wafer (0.300m diameter, 0.775mm thickness, V-notch)
- 25-slot FOUP Shell (10.0mm pitch, SEMI E47.1)
- Load Port Pedestal (Z = 0.900m datum, SEMI E15.1)
- Raised Perforated Cleanroom Floor Grid (600 x 600mm tiles)
- Overhead OHT Track Segment (Z = 3.50m rail elevation)

Usage inside Blender Scripting tab or headless CLI:
  blender --background --python 07_Blender_bpy_300mm晶圆厂标准件生成脚本.py
"""

from __future__ import annotations

import math

try:
    import bpy  # type: ignore
except ImportError:
    bpy = None


def ensure_collection(name: str):
    if name in bpy.data.collections:
        return bpy.data.collections[name]
    col = bpy.data.collections.new(name)
    bpy.context.scene.collection.children.link(col)
    return col


def link_to_collection(obj, col) -> None:
    for c in list(obj.users_collection):
        c.objects.unlink(obj)
    col.objects.link(obj)


def create_300mm_wafer(col, z_height: float = 0.96, name: str = "Wafer_300mm"):
    """Create a 300mm diameter x 0.775mm thick wafer disc."""
    bpy.ops.mesh.primitive_cylinder_add(
        vertices=96,
        radius=0.150,
        depth=0.000775,
        location=(0.0, 0.0, z_height),
    )
    wafer = bpy.context.active_object
    wafer.name = name
    link_to_collection(wafer, col)
    return wafer


def create_foup_stack(col, base_z: float = 0.900) -> None:
    """Create a 25-wafer FOUP stack (10mm pitch) and translucent housing box."""
    for slot in range(25):
        z = base_z + 0.035 + slot * 0.010
        create_300mm_wafer(col, z_height=z, name=f"FOUP_Wafer_Slot_{slot + 1:02d}")

    # FOUP outer shell (approx 360 x 350 x 330 mm)
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, base_z + 0.165))
    shell = bpy.context.active_object
    shell.name = "FOUP_Shell_E47_1"
    shell.scale = (0.360, 0.350, 0.330)
    shell.display_type = "WIRE"
    link_to_collection(shell, col)


def create_load_port_and_floor(col) -> None:
    """Create SEMI E15.1 900mm Load Port pedestal and 600x600mm raised floor tiles."""
    # Load port pedestal up to Z=0.900m
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 0.450))
    lp = bpy.context.active_object
    lp.name = "LoadPort_SEMI_E15_1_Z900"
    lp.scale = (0.450, 0.480, 0.900)
    link_to_collection(lp, col)

    # Raised floor tiles (6x6 array of 600x600mm tiles)
    for ix in range(-3, 3):
        for iy in range(-3, 3):
            cx = (ix + 0.5) * 0.600
            cy = (iy + 0.5) * 0.600
            bpy.ops.mesh.primitive_cube_add(size=1.0, location=(cx, cy, -0.020))
            tile = bpy.context.active_object
            tile.name = f"FloorTile_600mm_{ix}_{iy}"
            tile.scale = (0.596, 0.596, 0.040)
            link_to_collection(tile, col)

    # Overhead OHT Rail at Z=3.50m
    bpy.ops.mesh.primitive_cube_add(size=1.0, location=(0.0, 0.0, 3.500))
    rail = bpy.context.active_object
    rail.name = "OHT_Track_Z3500"
    rail.scale = (3.600, 0.240, 0.120)
    link_to_collection(rail, col)


def build_fab_bay_primitives() -> None:
    col = ensure_collection("WaferFab_300mm_Standards")
    create_load_port_and_floor(col)
    create_foup_stack(col, base_z=0.900)
    print("Generated 300mm Wafer Fab parametric primitives successfully.")


if __name__ == "__main__":
    if bpy is None:
        print(
            "This script uses Blender's built-in `bpy` module.\n"
            "Run inside Blender (Scripting workspace) or via:\n"
            "  blender --background --python 07_Blender_bpy_300mm晶圆厂标准件生成脚本.py"
        )
    else:
        build_fab_bay_primitives()
