"""
# Bodies: utilities.
/src/utilities/camera.py
"""
import pyxel

from utilities.vectors import Vector2D
from utilities.objects import UpdatableObject

class Camera(UpdatableObject):
    """
    # Simulation's global `Camera`.
    """
    speed_pan: float = 3.0
    speed_scroll: float = 0.9
    drag: float = 0.1
    position: Vector2D
    velocity: Vector2D
    zoom: float

    def __init__(self) -> None:
        """
        Instantiate the global `Camera`.
        """
        self.position = Vector2D(0.0, 0.0)
        self.velocity = Vector2D(0.0, 0.0)
        self.zoom = 1.0
    
        return
    
    def listen_keys(self) -> None:
        """
        Move the camera listening to inputs.
        """
        if pyxel.btn(pyxel.KEY_UP):
            self.velocity.y = -self.speed_pan
        if pyxel.btn(pyxel.KEY_DOWN):
            self.velocity.y = self.speed_pan
        if pyxel.btn(pyxel.KEY_LEFT):
            self.velocity.x = -self.speed_pan
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.velocity.x = self.speed_pan

        if pyxel.mouse_wheel != 0:
            self.zoom *= self.speed_scroll ** pyxel.mouse_wheel


    def update(self) -> None:
        self.listen_keys()

        self.position += self.velocity

        self.velocity *= self.drag

        return
