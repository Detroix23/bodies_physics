"""
# Bodies: utilities.
/src/utilities/objects.py
"""
import abc

from utilities.vectors import Vector2D

class DrawableObject(abc.ABC):
    """
    # `DrawableObject` in `pyxel`.
    """
    @abc.abstractmethod
    def draw(self) -> None:
        """
        Draw `self` and its components to the screen.
        """

class UpdatableObject(abc.ABC):
    """
    # `UpdatableObject` in the game loop.
    """
    @abc.abstractmethod
    def update(self) -> None:
        """
        Handles the logic for `self`.
        """

class SceneObject(UpdatableObject, DrawableObject):
    """
    # `SceneObject`.
    Is both:
    - `UpdatableObject`;
    - `DrawableObject`.
    """

class Entity(SceneObject):
    """
    # `Entity`: `SceneObject` with physic properties.
    """
    @abc.abstractmethod
    def get_id(self) -> int:
        """
        Get immutable unique `self` ID.
        """
    
    @abc.abstractmethod
    def get_mass(self) -> float:
        """
        Get `self` total mass.
        """
    
    @abc.abstractmethod
    def get_position(self) -> Vector2D:
        """
        Get current `self` position for linear motion.
        """
    
    @abc.abstractmethod
    def set_position(self, vector: Vector2D) -> None:
        """
        Update `self` position for linear motion.
        """

    @abc.abstractmethod
    def get_velocity(self) -> Vector2D:
        """
        Get current `self` velocity for linear motion.
        """
    
    @abc.abstractmethod
    def set_velocity(self, vector: Vector2D) -> None:
        """
        Update `self` `velocity` for linear motion.
        """

    @abc.abstractmethod
    def get_acceleration(self) -> Vector2D:
        """
        Get current `self` acceleration for linear motion.
        """
    
    @abc.abstractmethod
    def set_acceleration(self, vector: Vector2D) -> None:
        """
        Update `self` acceleration for linear motion.
        """

    @abc.abstractmethod
    def get_force(self) -> Vector2D:
        """
        Get current `self` force for linear motion.
        """
    
    @abc.abstractmethod
    def set_force(self, vector: Vector2D) -> None:
        """
        Update `self` force for linear motion.
      """

    @abc.abstractmethod
    def get_rotation(self) -> float:
        """
        Get current `self` rotation for angular motion.
        """
    
    @abc.abstractmethod
    def set_rotation(self, value: float) -> None:
        """
        Update `self` rotation for angular motion.
        """

    @abc.abstractmethod
    def get_angular_velocity(self) -> float:
        """
        Get current `self` angular velocity for angular motion.
        """
    
    @abc.abstractmethod
    def set_angular_velocity(self, value: float) -> None:
        """
        Update `self` angular velocity for angular motion.
        """

    @abc.abstractmethod
    def get_angular_acceleration(self) -> float:
        """
        Get current `self` angular acceleration for angular motion.
        """
    
    @abc.abstractmethod
    def set_angular_acceleration(self, value: float) -> None:
        """
        Update `self` angular acceleration for angular motion.
        """

    @abc.abstractmethod
    def get_torque(self) -> float:
        """
        Get current `self` torque for angular motion.
        """
    
    @abc.abstractmethod
    def set_torque(self, value: float) -> None:
        """
        Update `self` torque for angular motion.
        """
