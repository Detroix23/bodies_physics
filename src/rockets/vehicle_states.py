"""
# Rockets
/src/rockets/vehicle_states.py
"""
from typing import Optional

from utilities.vectors import Vector2D
from utilities import general, matrices


class VehicleState:
    """
    # Shared `VehicleState` across `Vehicle`, `Node`, `Thruster`.
    """
    drag_coefficient: float
    """ dimension-less """

    position: Vector2D
    """ in **m** """
    velocity: Vector2D
    """ in **m/s** """
    acceleration: Vector2D
    """ in **m/s²** """
    force: Vector2D
    """ in 1**N** = 1**kg·m/s²** """

    rotation: float
    """ dimension-less """
    angular_velocity: float
    """ in **1/s** """
    angular_acceleration: float
    """ in **1/s²** """
    torque: float
    """ in **kg·m²/s²** """

    mass_total: float
    """ in **kg** """
    center_mass: Vector2D
    """ Relative to the anchor (`position`), in **m** """
    moment_inertia: float
    """ in **kg·m²** """

    def __init__(
        self,
        drag_coefficient: float,
        position: Vector2D,
        velocity: Optional[Vector2D] = None,
        acceleration: Optional[Vector2D] = None,
        force: Optional[Vector2D] = None,
        rotation: Optional[float] = None,
        angular_velocity: Optional[float] = None,
        angular_acceleration: Optional[float] = None,
        torque: Optional[float] = None,
        mass_total: Optional[float] = None,
        center_mass: Optional[Vector2D] = None,
        moment_inertia: Optional[float] = None,
    ) -> None:
        """
        Create and sets to zero the common `VehicleState`.
        """
        self.drag_coefficient = drag_coefficient
    
        self.position = position
        self.velocity = general.default(velocity, Vector2D.null())
        self.acceleration = general.default(acceleration, Vector2D.null())
        self.force = general.default(force, Vector2D.null())

        self.rotation = general.default(rotation, 0.0)
        self.angular_velocity = general.default(angular_velocity, 0.0)
        self.angular_acceleration = general.default(angular_acceleration, 0.0)
        self.torque = general.default(torque, 0.0)

        if mass_total is not None:
            self.mass_total = mass_total
        if center_mass is not None:
            self.center_mass = center_mass
        if moment_inertia is not None:
            self.moment_inertia = moment_inertia

        return
    
    def get_absolute_com(self) -> Vector2D:
        """
        Get the absolute position of the center of mass.
        """
        return self.position + self.center_mass

    def get_relative_anchor(self) -> Vector2D:
        """
        Get the arbitrary (0;0) body anchor 
        relative to the center of mass. 
        """
        return matrices.rotate(
            self.center_mass * (-1), 
            self.rotation
        )

    def get_absolute_anchor(self) -> Vector2D:
        """
        Get the absolute position of the anchor 
        rotated around the center of mass.
        """
        return self.get_absolute_com() + self.get_relative_anchor()
