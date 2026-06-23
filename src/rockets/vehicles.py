"""
# Rockets
/src/rockets/vehicles.py
"""
import pyxel

from utilities.vectors import Vector2D
from utilities.objects import Entity
from utilities import draw
from rockets.state import State
from rockets.vehicle_states import VehicleState
from rockets.nodes import Node

NodeLinks = dict[int, list[int]]
""" Graph-dictionary with node's IDs. """


class Vehicle(Entity):
    """
    # Rocket `Vehicle` body composed of `Nodes`.
    """
    _id: int
    state: State
    vehicle_state: VehicleState
    nodes: dict[int, Node]
    node_links: NodeLinks
    
    def __init__(
        self,
        id: int,
        state: State,
        vehicle_state: VehicleState,
        nodes: list[Node],
        node_links: NodeLinks,
    ) -> None:
        """
        Create the `Vehicle` and compute its centers.
        """
        self._id = id
        self.state = state
        self.vehicle_state = vehicle_state
        self.nodes = {node.get_id(): node for node in nodes}
        self.node_links = node_links

        self.find_center_of_mass()

        return
    
    def get_id(self) -> int:
        return self._id
    
    def get_position(self) -> Vector2D:
        return self.vehicle_state.position
    
    def set_position(self, vector: Vector2D) -> None:
        self.vehicle_state.position = vector
        return
    
    def get_velocity(self) -> Vector2D:
        return self.vehicle_state.velocity
    
    def set_velocity(self, vector: Vector2D) -> None:
        self.vehicle_state.velocity = vector
        return

    def find_center_of_mass(self) -> Vector2D:
        """
        Determine the center of mass of `Vehicle` according to its `nodes`,
        set and returns the relative position of the center of mass.
        """
        position: Vector2D = Vector2D(0.0, 0.0)
        mass: float = 0.0
        for node in self.nodes.values():
            position += node.get_position() * node.mass
            mass += node.mass

        self.vehicle_state.center_mass = position / mass
        return self.vehicle_state.center_mass

    def apply_velocity(self) -> None:
        """
        Displace the `Vehicle` with `velocity`.
        """
        self.vehicle_state.position += self.get_velocity()
        
        return

    def apply_bounds(self) -> None:
        """
        Clamp position in the world bounds.
        """
        if self.vehicle_state.position.y <= 0.0:
            self.vehicle_state.position.y = 0.0
            self.vehicle_state.velocity.y = 0.0

        return

    def update(self) -> None:
        node_velocity: Vector2D = Vector2D(0.0, 0.0)
        
        for node in self.nodes.values():
            node.update()
            node_velocity += node.get_velocity()
        
        self.set_velocity(node_velocity / len(self.nodes))

        self.apply_velocity()
        self.apply_bounds()

        return
    
    def draw(self) -> None:
        info_size: int = 4

        # Center of vehicle.
        draw.rectangle(
            self.state.camera,
            self.get_position().x - info_size // 2,
            self.get_position().y - info_size // 2,
            info_size,
            info_size,
            pyxel.COLOR_LIGHT_BLUE,
        )

        # Center of mass.
        draw.rectangle(
            self.state.camera,
            self.get_position().x + self.vehicle_state.center_mass.x - info_size // 2,
            self.get_position().y + self.vehicle_state.center_mass.y - info_size // 2,
            info_size,
            info_size,
            pyxel.COLOR_RED,
        )

        # Node links.
        for node, links in self.node_links.items():
            for link in links:
                center: Vector2D = self.vehicle_state.position - self.vehicle_state.center_mass
                node_position: Vector2D = self.nodes[node].get_position()
                link_position: Vector2D = self.nodes[link].get_position()
                
                draw.line(
                    self.state.camera,
                    center.x + node_position.x,
                    center.y + node_position.y,
                    center.x + link_position.x,
                    center.y + link_position.y,
                    pyxel.COLOR_WHITE,
                )

        # Node bodies.
        for node in self.nodes.values():
            node.draw()

        return
    