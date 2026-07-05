"""
# Rockets
/src/rockets/state.py
"""
from typing import Optional

from utilities.definitions import GRAVITY_EARTH, AIR_DENSITY_0
from utilities.objects import Entity
from utilities.camera import Camera
from utilities import general

class State:
    """
    # Global simulation `State`.
    """
    delta_time: float
    gravitational_constant: float
    air_density: float
    camera: Camera
    entities: dict[int, Entity]
    
    def __init__(
        self,
        delta_time: Optional[float] = None,
        gravitational_constant: Optional[float] = None,
        air_density: Optional[float] = None,
    ) -> None:
        """
        Instantiate the global `State`. 
        Should call be called only once during the whole execution.
        **Resets the `State`.**
        """
        self.delta_time = general.default(delta_time, 0.1)
        self.gravitational_constant = general.default(
            gravitational_constant, 
            GRAVITY_EARTH,
        )
        self.air_density = general.default(
            air_density,
            AIR_DENSITY_0,
        )
        self.camera = Camera()
        self.entities = dict()

        return
