"""
# Rockets
/src/rockets/vehicles.py
"""
import math

import pyxel

from utilities.definitions import GRAVITATIONAL_CONSTANT, AIR_DENSITY_0
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

        self.find_mass_total()
        self.find_center_of_mass()
        self.find_moment_of_inertia()

        return
    
    def get_id(self) -> int:
        return self._id
    
    def get_mass(self) -> float:
        return self.vehicle_state.mass_total

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

    def get_acceleration(self) -> Vector2D:
        return self.vehicle_state.acceleration
    
    def set_acceleration(self, vector: Vector2D) -> None:
        self.vehicle_state.acceleration = vector
        return

    def get_force(self) -> Vector2D:
        return self.vehicle_state.force
    
    def set_force(self, vector: Vector2D) -> None:
        self.vehicle_state.force = vector
        return

    def get_rotation(self) -> float:
        return self.vehicle_state.rotation
    
    def set_rotation(self, value: float) -> None:
        self.vehicle_state.rotation = value
        return

    def get_angular_velocity(self) -> float:
        return self.vehicle_state.angular_velocity
    
    def set_angular_velocity(self, value: float) -> None:
        self.vehicle_state.angular_velocity = value
        return
    
    def get_angular_acceleration(self) -> float:
        return self.vehicle_state.angular_acceleration
    
    def set_angular_acceleration(self, value: float) -> None:
        self.vehicle_state.angular_acceleration = value
        return

    def get_torque(self) -> float:
        return self.vehicle_state.torque

    def set_torque(self, value: float) -> None:
        self.vehicle_state.torque = value
        return 

    def get_center_of_mass(self) -> Vector2D:
        """
        Returns the position of the center of mass.
        """
        return self.vehicle_state.center_mass

    def get_moment_of_inertia(self) -> float:
        """
        Returns a scalar: the moment of inertia used in angular motion.
        """
        return self.vehicle_state.moment_inertia

    def relative_to_center_of_mass(
        self, 
        position: Vector2D
    ) -> Vector2D:
        """
        Returns the given center-relative `position` 
        shifted to be relative to the center of mass. 
        """
        return (position
            + self.get_position() 
            - self.get_center_of_mass()
        )

    def find_mass_total(self) -> float:
        """
        Sums up all the node's masses.
        """
        self.vehicle_state.mass_total = sum(node.mass for node in self.nodes.values())
        return self.vehicle_state.mass_total
    
    def find_center_of_mass(self) -> Vector2D:
        """
        Determine the center of mass of `Vehicle` according to its `nodes`,
        set and returns the relative position of the center of mass.
        """
        position: Vector2D = Vector2D.null()
        mass: float = 0.0
        for node in self.nodes.values():
            position += node.get_position() * node.mass
            mass += node.mass

        self.vehicle_state.center_mass = position / mass
        return self.vehicle_state.center_mass

    def find_moment_of_inertia(self) -> float:
        """
        Use a discrete sum to find the scalar 2D moment of inertia.
        """
        self.vehicle_state.moment_inertia = sum(
            (
                node.mass 
                * self.relative_to_center_of_mass(node.get_position()
                    ).magnitude2()
            )
            for node in self.nodes.values()
        )
        return self.vehicle_state.moment_inertia

    def update_nodes(self) -> None:
        """
        Trigger an update for all nodes, implicitly for all thrusters.
        """
        for node in self.nodes.values():
            node.update()

        return

    def apply_bounds(self) -> None:
        """
        Clamp position in the world bounds.
        """
        if self.vehicle_state.position.y <= 0.0:
            self.vehicle_state.position.y = 0.0
            self.vehicle_state.velocity.y = 0.0

        return

    def apply_gravity(self) -> None:
        """
        Apply gravitational force.
        """
        self.vehicle_state.force += (
            Vector2D(0.0, -GRAVITATIONAL_CONSTANT) 
            * self.vehicle_state.mass_total
        )
        return
    
    def apply_drag(self) -> Vector2D:
        """
        Apply air drag with the current velocity.
        """
        force: Vector2D = (
            self.get_velocity()
            * (-1/ 2) 
            * self.get_velocity().magnitude()
            * AIR_DENSITY_0
            * self.vehicle_state.drag_coefficient
        )
        self.vehicle_state.force += force
        return force

    def apply_thrust(self) -> None:
        """
        Update force and torque from thrusters from all nodes.
        """
        for node in self.nodes.values():
            # Position of the node relative to the center of mass.
            position: Vector2D = self.relative_to_center_of_mass(node.get_position())

            for thruster in node.thrusters.values():
                if thruster.is_on():
                    # Force vector of the thruster.
                    force: Vector2D = Vector2D(
                        math.cos(thruster.direction),
                        math.sin(thruster.direction),
                    ) * thruster.force
                    # Torque scalar by the cross product r × F.
                    torque: float = position.cross(force)

                    self.vehicle_state.force += force
                    self.vehicle_state.torque += torque

    def update_linear_motion(self) -> None:
        """
        Apply linear displacement of force, acceleration, velocity, position.
        """
        self.set_acceleration(
            self.get_force() 
            / self.get_mass()
        )
        self.vehicle_state.velocity += (
            self.get_acceleration() 
            * self.state.delta_time
        )
        self.vehicle_state.position += (
            self.get_velocity() * self.state.delta_time
            + self.get_acceleration() * 0.5 * self.state.delta_time * self.state.delta_time
        )

        return

    def update_angular_motion(self) -> None:
        """
        Apply angular displacement of torque, acceleration, velocity, rotation.
        """
        self.set_angular_acceleration(
            self.get_torque() 
            / self.get_moment_of_inertia()
        )
        self.vehicle_state.angular_velocity += (
            self.get_angular_acceleration() 
            * self.state.delta_time
        )
        self.vehicle_state.rotation += (
            self.get_angular_velocity() * self.state.delta_time
            + self.get_angular_acceleration() * 0.5 * self.state.delta_time * self.state.delta_time
        )

        return

    def update(self) -> None:
        self.update_nodes()

        self.set_force(Vector2D.null())
        self.set_torque(0.0)

        self.apply_gravity()
        self.apply_drag()
        self.apply_thrust()

        self.update_linear_motion()
        self.update_angular_motion()    
        
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
    