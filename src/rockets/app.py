"""
# Rockets
/src/rockets/app.py
"""
import pyxel

from utilities.vectors import Vector2D
from utilities.objects import Entity, SceneObject
from utilities import draw
from rockets.state import State
from rockets.thrusters import Thruster
from rockets.node import Node

class App(SceneObject):
    """
    # `App`: first `SceneObject`.
    """
    state: State

    def __init__(self) -> None:
        """
        Create the `App`, initialize the simulation.

        Does not run it: start with `run`.
        """
        self.state = State()
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

    def run(self) -> None:
        """
        Starts the `App` simulation with `update` and `draw`.
        """
        print("(?) rockets.app.App.run() Start...")

        self.state.entities[0] = Node(
            id=0,
            state=self.state,
            rotation=0.0,
            position=Vector2D(50.0, 50.0),
            drag=0.9,
            mass=2.0,
            thrusters={
                0: Thruster(
                    id=0,
                    direction=0.0,
                    force=30.0,
                    key=pyxel.KEY_W,
                ),
            },
            links={},
        )

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        self.state.camera.update()

        for entity in self.state.entities.values():
            entity.update()
        
        return
    
    def draw_text(self) -> None:
        """
        Draw all UI text.
        """
        node1: Entity = self.state.entities[0]
        
        for index, text in enumerate([
            "Camera: ",
            f"p={self.state.camera.position.decimal(2)}",
            f"z={self.state.camera.zoom:.4f}",
            "Node1: ",
            f"p={node1.get_position().decimal(2)}",
            f"v={node1.get_velocity().decimal(2)}",
        ]):
            pyxel.text(10, 10 + index * 10, text, pyxel.COLOR_WHITE)

        return

    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)

        draw.rectangle(
            self.state.camera,
            -5, 5,
            10, 10,
            pyxel.COLOR_WHITE,
        )
        draw.rectangle(
            self.state.camera,
            -500, 0,
            1000, 2,
            pyxel.COLOR_DARK_BLUE,
        )

        for entity in self.state.entities.values():
            entity.draw()

        self.draw_text()

        return
