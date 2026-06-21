"""
# Rockets
/src/rockets/app.py
"""
import pyxel

from utilities.objects import SceneObject
from rockets.state import State

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
        pyxel.run(self.update, self.draw)

    def update(self) -> None:
        return
    
    def draw(self) -> None:
        return