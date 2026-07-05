"""
# Bodies: utilities.
/src/utilities/general.py
"""
from typing import TypeVar, Optional, Union

_T_DEFAULT = TypeVar("_T_DEFAULT")

def default(value: Optional[_T_DEFAULT], default: _T_DEFAULT) -> _T_DEFAULT:
    """
    Returns `value` if not `None`, else `default`.
    """
    return (value
        if value is not None
        else default
    )

def sign(value: Union[float, int]) -> int:
    """
    Returns the sign of `value`.
    """
    if value < 0:
        return -1
    elif value > 0:
        return 1
    else:
        return 0
