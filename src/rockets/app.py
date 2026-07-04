"""
# Rockets
/src/rockets/app.py
"""
import pyxel

from utilities.objects import SceneObject
from utilities import draw
from rockets.state import State
from rockets import presets


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
        self.state = State(
            delta_time=0.01,
        )
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
        # self.state.entities[0] = presets.vehicle_simple1_1_1(self.state)

        self.state.entities[1] = presets.vehicle_rocket1_2_2(self.state)
        
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
                f"- mas={entity.get_mass():.2f}kg",
                "Linear:",
                f"- pos={entity.get_position().decimal(2)}m",
                f"- vel={entity.get_velocity().decimal(2)}m/s",
                f"- acc={entity.get_acceleration().decimal(2)}m/s²",
                f"- for={entity.get_force().decimal(2)}N",
                "Angular",
                f"- rot={entity.get_rotation():.2f}",
                f"- vel={entity.get_angular_velocity():.2f}/s",
                f"- acc={entity.get_angular_acceleration():.2f}/s²",
                f"- tor={entity.get_torque():.2f}kg*m²/s²"
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
