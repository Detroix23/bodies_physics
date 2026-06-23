"""
# Rockets
/src/rockets/node.py
"""
import math

import pyxel

from utilities.definitions import GRAVITATIONAL_CONSTANT, UP_SHIFT
from utilities.vectors import Vector2D
from utilities.objects import Entity
from utilities import draw
from rockets.state import State
from rockets.vehicle_states import VehicleState
from rockets.thrusters import Thruster

class Node(Entity):
    """
    # Rocket body `Node`.
    Can hold thruster.
    """
    _id: int
    state: State
    vehicle_state: VehicleState
    relative_position: Vector2D
    """ relative, in **m**. """
    velocity: Vector2D
    """ in **m/s**. """
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
        self.relative_position = relative_position
        self.velocity = Vector2D(0.0, 0.0)
        self.drag = drag
        self.size = size
        self.mass = mass
        self.thrusters = thrusters
        
        return
    
    def get_id(self) -> int:
        return self._id
    
    def get_position(self) -> Vector2D:
        return self.relative_position
    
    def set_position(self, vector: Vector2D) -> None:
        self.relative_position = vector
        return
    
    def get_velocity(self) -> Vector2D:
        return self.velocity
    
    def set_velocity(self, vector: Vector2D) -> None:
        self.velocity = vector
        return

    def apply_thrust(self) -> None:
        """
        Check the `thrusters` and eventually apply the force.
        """
        for thruster in self.thrusters.values():
            if thruster.is_on():
                speed: float = thruster.force / self.mass
                direction: float = self.vehicle_state.rotation + thruster.direction 
                self.velocity += Vector2D(
                    math.cos(direction + UP_SHIFT) * speed,
                    math.sin(direction + UP_SHIFT) * speed,
                )
        
        return

    def apply_world(self) -> None:
        """
        Apply air drag and gravity to the `velocity` vector.
        """
        self.velocity.y -= GRAVITATIONAL_CONSTANT
            
        self.velocity *= (1.0 - self.drag)

        return

    def update(self) -> None:
        for thruster in self.thrusters.values():
            thruster.update()

        self.apply_thrust()
        self.apply_world()

        return

    def draw(self) -> None:
        center: Vector2D = (
            self.vehicle_state.position
            + self.relative_position 
            - self.vehicle_state.center_mass
        )
        
        draw.rectangle(
            self.state.camera,
            center.x - self.size / 2,
            center.y + self.size / 2,
            self.size,
            self.size,
            pyxel.COLOR_CYAN,
        )

        return
    