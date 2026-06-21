"""
# Rockets
/src/rockets/__main__.py
"""

from rockets.app import App

def main() -> None:
    """
    Main entry point for the rocket simulation.
    """
    app = App()
    app.run()

    return

main()
