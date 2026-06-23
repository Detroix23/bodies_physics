"""
# Rockets
/src/rockets/app.py
"""
import math

import pyxel

from utilities.vectors import Vector2D
from utilities.objects import SceneObject
from utilities import draw
from rockets.state import State
from rockets.vehicle_states import VehicleState
from rockets.thrusters import Thruster
from rockets.nodes import Node
from rockets.vehicles import Vehicle

class App(SceneObject):
    """
    # `App`: first `SceneObject`.
    """
    state: State
    lines: list[str]

    def __init__(self) -> None:
        """
        Create the `App`, initialize the simulation.

        Does not run it: start with `run`.
        """
        self.state = State()
        self.lines = []
        print("(?) rockets.app.App.__init__() State initialized.")

        pyxel.init(
            512,
            512,
            title="Bodies simulation: rockets.",
            fps=30,
            quit_key=pyxel.KEY_ESCAPE,
        )
        print("(?) rockets.app.App.__init__() Pyxel initialized.")

        return

    def load_start(self) -> None:
        """
        Load the arbitrary chosen starting assets.
        """
        vehicle1_state: VehicleState = VehicleState(
            position=Vector2D(-50.0, 5000),
            velocity=Vector2D(0.0, 10.0),
            acceleration=Vector2D(0.0, 0.0),
            rotation=0.0
        )

        self.state.entities[0] = Vehicle(
            id=0,
            state=self.state,
            vehicle_state=vehicle1_state,
            nodes=[
                Node(
                    id=0,
                    state=self.state,
                    vehicle_state=vehicle1_state,
                    relative_position=Vector2D(0.0, 0.0),
                    drag=0.1,
                    mass=2.0,
                    size=7.0,
                    thrusters={
                        0: Thruster(
                            id=0,
                            state=self.state,
                            vehicle_state=vehicle1_state,
                            direction=0.0,
                            force=30.0,
                            key=pyxel.KEY_W,
                        ),
                    },
                ),
            ],
            node_links={}
        )   

        vehicle2_state: VehicleState = VehicleState(
            position=Vector2D(75.0, 5000.0),
            velocity=Vector2D(0.0, 10.0),
            acceleration=Vector2D(0.0, 0.0),
            rotation=0.0
        )

        self.state.entities[1] = Vehicle(
            id=1,
            state=self.state,
            vehicle_state=vehicle2_state,
            nodes=[
                Node(
                    id=0,
                    state=self.state,
                    vehicle_state=vehicle2_state,
                    relative_position=Vector2D(0.0, 0.0),
                    drag=0.1,
                    mass=2.0,
                    size=7.0,
                    thrusters={
                        0: Thruster(
                            id=0,
                            state=self.state,
                            vehicle_state=vehicle2_state,
                            direction=0.0,
                            force=50.0,
                            key=pyxel.KEY_E,
                        ),
                    },
                ),
                Node(
                    id=1,
                    state=self.state,
                    vehicle_state=vehicle2_state,
                    relative_position=Vector2D(25.0, 5.0),
                    drag=0.1,
                    mass=2.0,
                    size=7.0,
                    thrusters={
                        0: Thruster(
                            id=0,
                            state=self.state,
                            vehicle_state=vehicle2_state,
                            direction=math.pi / 2,
                            force=15.0,
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

        return

    def run(self) -> None:
        """
        Starts the `App` simulation with `update` and `draw`.
        """
        print("(?) rockets.app.App.run() Start...")

        self.load_start()

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.state.camera.update()

        for entity in self.state.entities.values():
            entity.update()

        # Text.
        self.lines = [
            "Camera: ",
            f"p={self.state.camera.position.decimal(2)}m",
            f"z={self.state.camera.zoom:.4f}",   
        ]
        for entity_id, entity in self.state.entities.items():
            self.lines += [
                f"Entity {entity_id}: ",
                f"- p={entity.get_position().decimal(2)}m",
                f"- v={entity.get_velocity().decimal(2)}m/s",
            ]

        return
    
    def draw_text(self) -> None:
        """
        Draw all UI text.
        """
        for index, text in enumerate(self.lines):
            pyxel.text(10, 10 + index * 10, text, pyxel.COLOR_WHITE)

        return

    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)

        # Center of world.
        draw.rectangle(
            self.state.camera,
            -2, 2,
            4, 4,
            pyxel.COLOR_WHITE,
        )
        # Line of ground.
        draw.rectangle(
            self.state.camera,
            self.state.camera.position.x - pyxel.width // 2 * self.state.camera.zoom, 
            0,
            pyxel.width * self.state.camera.zoom, 
            2,
            pyxel.COLOR_DARK_BLUE,
        )

        for entity in self.state.entities.values():
            entity.draw()

        self.draw_text()

        return
