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
    def get_position(self) -> Vector2D:
        """
        Get current `self` position.
        """
    
    @abc.abstractmethod
    def set_position(self, vector: Vector2D) -> None:
        """
        Update `self` `position`.
        """

    @abc.abstractmethod
    def get_velocity(self) -> Vector2D:
        """
        Get current `self` velocity.
        """
    
    @abc.abstractmethod
    def set_velocity(self, vector: Vector2D) -> None:
        """
        Update `self` `velocity`.
        """
