"""
# Rockets
/src/rockets/node.py
"""
import math

import pyxel

from utilities.definitions import UP_SHIFT
from utilities.vectors import Vector2D
from utilities.objects import SceneObject
from utilities import draw, matrices
from rockets.state import State
from rockets.vehicle_states import VehicleState
from rockets.thrusters import Thruster

class Node(SceneObject):
    """
    # Rocket body `Node`.
    Can hold thruster.
    """
    _id: int
    state: State
    vehicle_state: VehicleState
    _relative_position: Vector2D
    """ Relative to the body center. """
    rotated_position: Vector2D
    """ Relative rotated to the body center. """
    absolute_position: Vector2D 
    """ Absolute rotated. """
    center: Vector2D
    """ relative, in **m**. """
    drag: float
    """ Dimension-less coefficient that scales`velocity`. """
    size: float
    """ **pixels**. """
    mass: float
    """ in **kg**. """
    thrusters: dict[int, Thruster]


    def __init__(
        self,
        id: int,
        state: State,
        vehicle_state: VehicleState,
        relative_position: Vector2D,
        drag: float,
        mass: float,
        size: float,
        thrusters: dict[int, Thruster],
    ) -> None:
        """
        Instantiate a rocket `Node`.
        """
        self._id = id
        self.state = state
        self.vehicle_state = vehicle_state
        self._relative_position = relative_position
        self.rotated_position = relative_position
        self.absolute_position = self.vehicle_state.position + relative_position
        self.center = Vector2D.null()
        self.drag = drag
        self.size = size
        self.mass = mass
        self.thrusters = thrusters
        
        return
    
    def get_id(self) -> int:
        return self._id
    
    def get_position(self) -> Vector2D:
        """
        Returns the read-only relative position.
        """
        return self._relative_position

    def update(self) -> None:
        for thruster in self.thrusters.values():
            thruster.update()

        self.rotated_position = matrices.rotate(
            self.get_position(), 
            self.vehicle_state.rotation
        )

        self.absolute_position = self.rotated_position + self.vehicle_state.position

        return

    def draw_thrust(self) -> None:
        """
        Check the `thrusters` and draw their force.
        """
        for thruster in self.thrusters.values():
            if thruster.is_on():
                direction: float = (
                    self.vehicle_state.rotation 
                    + thruster.direction 
                    + UP_SHIFT
                )

                thrust: Vector2D = Vector2D(
                    math.cos(direction),
                    math.sin(direction),
                ) * -thruster.force

                draw.line(
                    self.state.camera,
                    self.center.x,
                    self.center.y,
                    self.center.x + thrust.x,
                    self.center.y + thrust.y,
                    pyxel.COLOR_ORANGE,
                )
        
        return
    

    def draw(self) -> None:
        self.center = (
            self.absolute_position
            - self.vehicle_state.center_mass
        )

        self.draw_thrust()

        draw.rectangle(
            self.state.camera,
            self.center.x - self.size / 2,
            self.center.y + self.size / 2,
            self.size,
            self.size,
            pyxel.COLOR_CYAN,
        )

        return
    