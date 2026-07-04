"""
# Rockets
/src/rockets/presets.py
"""
import math

import pyxel

from utilities.vectors import Vector2D
from rockets.state import State
from rockets.vehicle_states import VehicleState
from rockets.nodes import Node
from rockets.thrusters import Thruster
from rockets.vehicles import Vehicle

def vehicle_simple1_1_1(state: State) -> Vehicle:
    vehicle_state: VehicleState = VehicleState(
        drag_coefficient=0.2,
        position=Vector2D(-50.0, 5000),
        velocity=Vector2D(0.0, 10.0),
        acceleration=Vector2D.null(),
        force=Vector2D.null(),
        rotation=0.0
    )

    return Vehicle(
        id=0,
        state=state,
        vehicle_state=vehicle_state,
        nodes=[
            Node(
                id=0,
                state=state,
                vehicle_state=vehicle_state,
                relative_position=Vector2D.null(),
                drag=0.1,
                mass=2.0,
                size=7.0,
                thrusters={
                    0: Thruster(
                        id=0,
                        state=state,
                        vehicle_state=vehicle_state,
                        direction=0.0,
                        force=30.0,
                        key=pyxel.KEY_W,
                    ),
                },
            ),
        ],
        node_links={}
    )   

def vehicle_weird1_2_2(state: State) -> Vehicle:
    vehicle_state: VehicleState = VehicleState(
            drag_coefficient=0.0,
            position=Vector2D(75.0, 5000.0),
            velocity=Vector2D(0.0, 10.0),
            acceleration=Vector2D.null(),
            force=Vector2D.null(),
            rotation=0.0
        )

    return Vehicle(
        id=1,
        state=state,
        vehicle_state=vehicle_state,
        nodes=[
            Node(
                id=0,
                state=state,
                vehicle_state=vehicle_state,
                relative_position=Vector2D.null(),
                drag=0.1,
                mass=2.0,
                size=7.0,
                thrusters={
                    0: Thruster(
                        id=0,
                        state=state,
                        vehicle_state=vehicle_state,
                        direction=0.0,
                        force=250.0,
                        key=pyxel.KEY_E,
                    ),
                },
            ),
            Node(
                id=1,
                state=state,
                vehicle_state=vehicle_state,
                relative_position=Vector2D(25.0, 5.0),
                drag=0.1,
                mass=2.0,
                size=7.0,
                thrusters={
                    0: Thruster(
                        id=0,
                        state=state,
                        vehicle_state=vehicle_state,
                        direction=math.pi / 2,
                        force=100.0,
                        key=pyxel.KEY_F,
                    ),
                },
            ),
        ],
        node_links={
            0: [1],
            1: [0],
        }
    )

def vehicle_rocket1_2_2(state: State) -> Vehicle:
    vehicle_state: VehicleState = VehicleState(
            drag_coefficient=0.0,
            position=Vector2D(75.0, 5000.0),
            velocity=Vector2D(0.0, 10.0),
            acceleration=Vector2D.null(),
            force=Vector2D.null(),
            rotation=0.0
        )

    return Vehicle(
        id=2,
        state=state,
        vehicle_state=vehicle_state,
        nodes=[
            Node(
                id=0,
                state=state,
                vehicle_state=vehicle_state,
                relative_position=Vector2D(0.0, 25.0),
                drag=0.1,
                mass=1.9,
                size=7.0,
                thrusters={},
            ),
            Node(
                id=1,
                state=state,
                vehicle_state=vehicle_state,
                relative_position=Vector2D.null(),
                drag=0.1,
                mass=2.0,
                size=7.0,
                thrusters={
                    0: Thruster(
                        id=0,
                        state=state,
                        vehicle_state=vehicle_state,
                        direction=0.0,
                        force=200.0,
                        key=pyxel.KEY_W,
                    ),
                    1: Thruster(
                        id=1,
                        state=state,
                        vehicle_state=vehicle_state,
                        direction=math.pi / 2.0,
                        force=100.0,
                        key=pyxel.KEY_D,
                    ),
                },
            ),
        ],
        node_links={
            0: [1],
            1: [0],
        }
    )

