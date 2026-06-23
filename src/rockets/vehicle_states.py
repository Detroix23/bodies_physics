"""
# Rockets
/src/rockets/vehicle_states.py
"""
from utilities.vectors import Vector2D

class VehicleState:
    """
    # Shared `VehicleState` across `Vehicle`, `Node`, `Thruster`.
    """
    position: Vector2D
    velocity: Vector2D
    acceleration: Vector2D
    rotation: float
    center_mass: Vector2D

    def __init__(
        self,
        position: Vector2D,
        velocity: Vector2D,
        acceleration: Vector2D,
        rotation: float,
    ) -> None:
        """
        Create and sets to zero the common `VehicleState`.
        """
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.rotation = rotation
        
        return
    