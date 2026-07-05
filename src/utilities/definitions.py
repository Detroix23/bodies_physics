"""
# Bodies: utilities.
/src/utilities/definitions.py
"""
import math
from typing import Final

GRAVITY_EARTH: Final[float] = 9.8
""" *g* in **m/s²** """

AIR_DENSITY_0: Final[float] = 1.225
""" Air density *ρ* at sea level in **kg/m³** """

UP_SHIFT: Final[float] = math.pi / 2
""" Value added to radian value to shift the 0° up. """
