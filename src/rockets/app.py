"""
# Rockets
/src/rockets/app.py
"""
import pyxel

from utilities.vectors import Vector2D
from utilities.objects import SceneObject
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
            0,
            0.0,
            Vector2D(50.0, 50.0),
            2.0,
            thrusters={
                0: Thruster(
                    0,
                    0.0,
                    10.0,
                    pyxel.KEY_UP,
                )
            },
            links={},
        )

        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        for entity in self.state.entities.values():
            entity.update()
        
        return
    
    def draw(self) -> None:
        pyxel.cls(pyxel.COLOR_BLACK)

        for entity in self.state.entities.values():
            entity.draw()

        return
