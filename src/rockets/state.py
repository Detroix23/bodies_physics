"""
# Rockets
/src/rockets/state.py
"""

from utilities.objects import Entity
from utilities.camera import Camera

class State:
    """
    # Global simulation `State`.
    """
    camera: Camera
    entities: dict[int, Entity]
    
    def __init__(self) -> None:
        """
        Instantiate the global `State`. 
        Should call be called only once during the whole execution.
        **Resets the `State`.**
        """
        self.camera = Camera()
        self.entities = {}
    