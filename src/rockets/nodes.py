"""
# Rockets
/src/rockets/node.py
"""
import pyxel

from utilities.definitions import UP_SHIFT
from utilities.vectors import Vector2D
from utilities.objects import SceneObject
from utilities import draw, matrices
from rockets.state import State
from rockets.vehicle_states import VehicleState
from rockets.thrusters import Thruster

class Node(SceneObject):
    """
    # Rocket body `Node`.
    Can hold thruster.
    """
    _id: int
    state: State
    vehicle_state: VehicleState
    _relative_position: Vector2D
    """ Relative to the body center. """
    rotated_position: Vector2D
    """ 
    Anchor-relative coordinates rotated around the anchor. 
    """
    anchor_absolute: Vector2D
    """ Absolute, in **m**. """
    drag: float
    """ Dimension-less coefficient that scales`velocity`. """
    size: float
    """ **pixels**. """
    mass: float
    """ in **kg**. """
    thrusters: dict[int, Thruster]


    def __init__(
        self,
        id: int,
        state: State,
        vehicle_state: VehicleState,
        relative_position: Vector2D,
        drag: float,
        mass: float,
        size: float,
        thrusters: dict[int, Thruster],
    ) -> None:
        """
        Instantiate a rocket `Node`.
        """
        self._id = id
        self.state = state
        self.vehicle_state = vehicle_state
        self._relative_position = relative_position
        self.rotated_position = relative_position
        self.anchor_absolute = Vector2D.null()
        self.drag = drag
        self.size = size
        self.mass = mass
        self.thrusters = thrusters
        
        return
    
    def get_id(self) -> int:
        """
        Get the unique read-only ID of the `Node`.
        """
        return self._id
    
    def get_position(self) -> Vector2D:
        """
        Returns the read-only relative position 
        to the un-rotated anchor.
        """
        return self._relative_position

    def update(self) -> None:
        for thruster in self.thrusters.values():
            thruster.update()

        self.anchor_absolute = self.vehicle_state.get_absolute_anchor()

        self.rotated_position = matrices.rotate(
            (
                self.get_position() 
                # + self.vehicle_state.center_mass
                # + self.vehicle_state.get_relative_anchor()
            ), 
            self.vehicle_state.rotation
        )

        return

    def draw_thrust(self) -> None:
        """
        Check the `thrusters` and draw their force.
        """
        for thruster in self.thrusters.values():
            if thruster.is_on():
                direction: float = (
                    self.vehicle_state.rotation 
                    + thruster.direction 
                    + UP_SHIFT
                )
                thrust: Vector2D = (
                    Vector2D.direction_normal(direction) 
                    * -thruster.force
                )

                draw.line(
                    self.state.camera,
                    self.anchor_absolute.x + self.rotated_position.x,
                    self.anchor_absolute.y + self.rotated_position.y,
                    self.anchor_absolute.x + self.rotated_position.x + thrust.x,
                    self.anchor_absolute.y + self.rotated_position.y + thrust.y,
                    pyxel.COLOR_ORANGE,
                )
        return
    

    def draw(self) -> None:
        self.draw_thrust()

        draw.rectangle(
            self.state.camera,
            self.anchor_absolute.x + self.rotated_position.x - self.size / 2,
            self.anchor_absolute.y + self.rotated_position.y + self.size / 2,
            self.size,
            self.size,
            pyxel.COLOR_CYAN,
        )
        return
    