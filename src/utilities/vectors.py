"""
# Bodies: utilities.
/src/utilities/vectors.py
"""
import math
from typing import Union, Self

import pyxel

Any2D = Union['Vector2D']

ScalarOrVector = Union[float, int, 'Vector2D']

class Vector2D:
    """
    Define a mutable `float` `Vector2D`.
    """
    x: float
    y: float

    def __init__(self, x: float, y: float) -> None:
        """
        Instantiate a `float` vector of coordinates `x`; `y`.
        """
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        """
        Formatted `str`: "(x;y)".
        """
        return f"({self.x};{self.y})"

    def __repr__(self) -> str:
        """
        `exec` compatible `str`.
        """
        return f"Vector2D(x={self.x}, y={self.y})"

    def __add__(
        self, 
        value: ScalarOrVector
    ) -> 'Vector2D':
        """
        Add values to the vector, emulating numeric objects.
        Do not update the content of the vector
        """
        if isinstance(value, Vector2D):
            return Vector2D(self.x + value.x, self.y + value.y)
        else:
            return Vector2D(self.x + float(value), self.y + float(value))

    def __sub__(
        self, 
        value: ScalarOrVector
    ) -> 'Vector2D':
        """
        Add values to the vector, emulating numeric objects.
        Do not update the content of the vector
        """
        if isinstance(value, Vector2D):
            return Vector2D(self.x - value.x, self.y - value.y)
        else:
            return Vector2D(self.x - float(value), self.y - float(value))
    
    def __mul__(
        self, 
        factor: float
    ) -> 'Vector2D':
        """
        Multiply the values of the vector, emulating numeric objects.
        Do not update the content of the vector
        """
        return Vector2D(self.x * factor, self.y * factor)

    def __truediv__(
        self, 
        factor: float
    ) -> 'Vector2D':
        """
        Divide all value of the vector, emulating numeric objects.
        Do not update the content of the vector
        """
        return Vector2D(self.x / factor, self.y / factor)

    @staticmethod
    def null() -> 'Vector2D':
        """
        Create the `0` vector.
        """
        return Vector2D(0.0, 0.0)

    @staticmethod
    def direction_normal(angle: float) -> 'Vector2D':
        """
        Creates a normal vector using trigonometry:
        - pointing `angle`;
        - with a length of `1`
        """
        return Vector2D(
            math.cos(angle),
            math.sin(angle),
        )

    def copy(self) -> 'Vector2D':
        """
        Return a true unlinked copy of `self`.
        """
        return Vector2D(
            self.x,
            self.y,
        )
    
    def magnitude(self) -> float:
        """
        Return the length of the vector.
        """
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def magnitude2(self) -> float:
        """
        Return the length of the vector squared.
        Faster because no `sqrt`.
        """
        return self.x ** 2 + self.y ** 2

    def normalize(self) -> None:
        """
        Update the vector so that its magnitude is 1.  
        """
        magnitude: float = self.magnitude()
        self.x = self.x / magnitude
        self.y = self.y / magnitude
        
    def get_normal(self) -> 'Vector2D':
        """
        Returns a normalized **copy** of the vector. 
        """
        copy: Vector2D = self.copy()
        copy.normalize()
        return copy 
    
    def to_list(self) -> list[float]:
        """
        Convert `self` to a `list`: `[x, y]`.
        """
        return [self.x, self.y]
    
    def to_dict(self) -> dict[str, float]:
        """
        Convert `self` to a `dict`: `{"x": x, "y": y}`.
        """
        return {"x": self.x, "y": self.y} 
    
    def to_tuple(self) -> tuple[float, float]:
        """
        Convert `self` to a `tuple`: `(x, y)`.
        """
        return (self.x, self.y)

    def add(self, value: ScalarOrVector) -> Self:
        """
        Add values to the vector.
        Do update the value of the vector.
        """
        if isinstance(value, Vector2D):
            self.x += value.x
            self.y += value.y
        else:
            self.x += float(value)
            self.y += float(value)

        return self
    
    def subtract(self, value: ScalarOrVector) -> Self:
        """
        Add values to the vector.
        Do update the value of the vector.
        """
        if isinstance(value, Vector2D):
            self.x -= value.x
            self.y -= value.y
        else:
            self.x -= float(value)
            self.y -= float(value)

        return self

    def multiply(self, factor: float) -> Self:
        """
        Multiply the values of the vector.
        Do update the value of the vector.
        """
        self.x = self.x * factor
        self.y = self.y * factor

        return self

    def divide(self, factor: float) -> Self:
        """
        Divide all value of the vector.
        Do update the value of the vector. 
        """
        self.x = self.x / factor
        self.y = self.y / factor
        
        return self
    
    def dot(self, other: 'Vector2D') -> float:
        """
        Compute the dot-product using the analytic way: 
        ```
        a.x * b.x + a.y * b.y.
        ```
        """
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: 'Vector2D') -> float:
        """
        2D cross product `a` × `b`.
        """
        return cross(self, other)

    def zero(self) -> None:
        """
        Set all coordinate to zero.  
        """
        self.x = 0.0
        self.y = 0.0

    def is_close(self, other: 'Vector2D', offset: float) -> bool:
        """
        Return if the `other` vector if close enough in `offset`. 
        """
        return (
            abs(self.x - other.x) < offset 
            and abs(self.y - other.y) < offset
        )

    def decimal(self, places: int) -> str:
        """
        Return a `str` of `self` with `places` digits after the zero.
        """ 
        return f"{self.x:.{places}f};{self.y:.{places}f}"

    def draw_on(
        self, 
        x: float, 
        y: float, 
        size: float, 
        color: int
    ) -> None:
        """
        Draw a line representing `self` attached on (`x`, `y`).
        """
        if not (math.isclose(self.x, 0) and math.isclose(self.y, 0)): 
            pyxel.line(
                x, 
                y, 
                x + self.x * size, 
                y + self.y * size, 
                col=color
            )


def cross(a: Any2D, b: Any2D) -> float:
    """
    2D cross product `a` × `b`.
    """
    return a.x * b.y - a.y * b.x
