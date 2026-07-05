"""
# Rockets
/src/rockets/__main__.py
"""
import sys
from typing import Optional

from rockets.app import App

def help() -> None:
    """
    CLI help menu.
    """
    print("""## Help.
          
### Arguments.

-h | --help: prints this help message;
          
-d {float}: sets delta time;
          
-g {float}: sets gravitational constant;
          
-p {float}: sets air resistance (rhô);
          
""")
    return

def main() -> None:
    """
    Main entry point for the rocket simulation.
    """
    arguments: list[str] = sys.argv

    print("Arguments:")
    print("\n* ".join(f"`{argument}`" for argument in arguments))

    delta_time: Optional[float] = None
    gravitational_constant: Optional[float] = None
    air_density: Optional[float] = None

    for index, argument in enumerate(arguments):
        if argument in {"-h", "--help"}:
            return help()
            
        try:
            if argument in {"-d"}:
                delta_time = float(arguments[index + 1])

            elif argument in {"-g"}:
                gravitational_constant = float(arguments[index + 1])

            elif argument in {"-p"}:
                air_density = float(arguments[index + 1])
    
        except IndexError:
            print(f"(!) Missing argument for `{argument}` ({index}).")
        
        except TypeError:
            print(f"(!) Wrong type for argument parameter `{argument}` ({index}).")
    
    app = App(
        delta_time,
        gravitational_constant,
        air_density,
    )
    app.run()

    return

main()
