"""
# Bodies: utilities.
/src/utilities/draw.py
"""
import pyxel

from utilities.vectors import Vector2D
from utilities.camera import Camera

def rectangle(
    camera: Camera,
    x: float,
    y: float,
    width: float,
    height: float,
    color: int,
) -> None:
    """
    Draw a rectangle using `pyxel`'s `rect` with:
    - axis `+y` oriented up;
    - camera.
    """
    origin: Vector2D = Vector2D(
        (x - camera.position.x) / camera.zoom + pyxel.width // 2,
        (-y - camera.position.y) / camera.zoom + pyxel.height // 2,
    )
    size: Vector2D = Vector2D(
        max(1, width / camera.zoom),
        max(1, height / camera.zoom),
    )

    pyxel.rect(
        origin.x,
        origin.y,
        size.x,
        size.y,
        color,
    )
    return

def line(
    camera: Camera,
    x: float,
    y: float,
    u: float,
    v: float,
    color: int,
) -> None:
    """
    Draw a line from (x;y) to (u;v) using `pyxel`'s `line` with:
    - axis `+y` oriented up;
    - camera.
    """
    pyxel.line(
        (x - camera.position.x) / camera.zoom + pyxel.width / 2 ,
        (-y - camera.position.y) / camera.zoom + pyxel.height / 2,
        (u - camera.position.x) / camera.zoom + pyxel.width / 2 ,
        (-v - camera.position.y) / camera.zoom + pyxel.height / 2,
        color,
    )
    return

