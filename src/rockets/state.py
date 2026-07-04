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
    delta_time: float
    camera: Camera
    entities: dict[int, Entity]
    
    def __init__(
        self,
        delta_time: float,
    ) -> None:
        """
        Instantiate the global `State`. 
        Should call be called only once during the whole execution.
        **Resets the `State`.**
        """
        self.delta_time = delta_time
        self.camera = Camera()
        self.entities = dict()

        return
