"""
# Bodies: utilities.
/src/utilities/objects.py
"""
import abc

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
