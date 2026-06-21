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
from rockets.thrusters import Thruster

class Node(Entity):
    """
    # Rocket body `Node`.
    Can hold thruster.
    """
    _id: int
    state: State
    rotation: float
    position: Vector2D
    velocity: Vector2D
    drag: float
    size: float
    mass: float
    thrusters: dict[int, Thruster]
    links: dict['Node', float]

    def __init__(
        self,
        id: int,
        state: State,
        rotation: float,
        position: Vector2D,
        drag: float,
        mass: float,
        thrusters: dict[int, Thruster],
        links: dict['Node', float],
    ) -> None:
        """
        Instantiate a rocket `Node`.
        """
        self._id = id
        self.state = state
        self.rotation = rotation
        self.position = position
        self.velocity = Vector2D(0.0, 0.0)
        self.drag = drag
        self.size = 15.0
        self.mass = mass
        self.thrusters = thrusters
        self.links = links

        return
    
    def get_id(self) -> int:
        return self._id
    
    def get_position(self) -> Vector2D:
        return self.position
    
    def set_position(self, vector: Vector2D) -> None:
        self.position = vector
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
                direction: float = self.rotation + thruster.direction 
                self.velocity += Vector2D(
                    math.cos(direction + UP_SHIFT) * speed,
                    math.sin(direction + UP_SHIFT) * speed,
                )

                # thruster.disable()

    def apply_world(self) -> None:
        """
        Apply air drag and gravity to the `velocity` vector.
        """
        self.velocity += Vector2D(0.0, -GRAVITATIONAL_CONSTANT)

        self.velocity *= self.drag

        return

    def apply_velocity(self) -> None:
        """
        Apply displacement.
        """
        self.position += self.velocity

        return


    def update(self) -> None:
        for thruster in self.thrusters.values():
            thruster.update()

        self.apply_thrust()
        self.apply_world()
        self.apply_velocity()

        return

    def draw(self) -> None:
        draw.rectangle(
            self.state.camera,
            self.position.x - self.size / 2,
            self.position.y - self.size / 2,
            self.size / 2,
            self.size / 2,
            pyxel.COLOR_CYAN,
        )

        return