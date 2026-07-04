"""
# Rockets
/src/rockets/thrusters.py
"""
import pyxel

from utilities.objects import UpdatableObject
from rockets.state import State
from rockets.vehicle_states import VehicleState

class Thruster(UpdatableObject):
    """
    # Rocket `Thruster`, attached to a `Node`.
    """
    id: int
    state: State
    vehicle_state: VehicleState
    direction: float
    """ Angle in radians added from the rocket's axis. """
    force: float
    """ In `force` **N** (Newtons): 1 **kg·m/s²**"""
    _on: bool
    key: int
    """ Keyboard `key` that enables the thruster. """

    def __init__(
        self,
        id: int,
        state: State,
        vehicle_state: VehicleState,
        direction: float,
        force: float,
        key: int = pyxel.KEY_NONE,
    ) -> None:
        """
        Instantiate the `Thruster`.
        """
        self.id = id
        self.state = state
        self.vehicle_state = vehicle_state
        self.direction = direction
        self.force = force
        self._on = False
        self.key = key

        return
    
    def enable(self) -> None:
        """
        Turn the thruster `on`.
        """
        if not self.is_on():
            print(f"(?) rockets.thruster.Thruster.enable()  id={self.id}")
        self._on = True
        return
    
    def disable(self) -> None:
        """
        Turn the thruster off.
        """
        if self.is_on():
            print(f"(?) rockets.thruster.Thruster.disable() id={self.id}")
        self._on = False
        return

    def is_on(self) -> bool:
        """
        Returns `True` if the thruster is `on`.
        """
        return self._on
    
    def update(self) -> None:
        """
        Handles the key press for this `Thruster`.
        """
        if pyxel.btn(self.key):
            self.enable()
        else:
            self.disable()

        return
