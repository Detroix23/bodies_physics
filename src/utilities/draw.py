"""
# Bodies: utilities.
/src/utilities/draw.py
"""
import pyxel

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
    Draw a rectangle using `pyxel`'s `rect` with axis `+y` oriented up.
    """
    pyxel.rect(
        (x - camera.position.x) / camera.zoom + pyxel.width / 2 ,
        (-y - camera.position.y) / camera.zoom + pyxel.height / 2,
        width / camera.zoom,
        height / camera.zoom,
        color,
    )
    return
