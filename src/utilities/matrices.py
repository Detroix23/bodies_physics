"""
# Bodies: utilities.
/src/utilities/matrices.py
"""
import math

from utilities.vectors import Vector2D

def rotate(vector: Vector2D, angle: float) -> Vector2D:
    """
    Rotate the given `vector` by `angle` in radians
    using a rotation matrix:

    ```
    ⎡ x'⎤   ⎡ cos(θ) -sin(θ) ⎤   ⎡ x ⎤
    ⎣ y'⎦ = ⎣ sin(θ)  cos(θ) ⎦ * ⎣ y ⎦
    ```
    """
    cos: float = math.cos(angle)
    sin: float = math.sin(angle)

    return Vector2D(
        vector.x * cos - vector.y * sin,
        vector.x * sin + vector.y * cos
    )
