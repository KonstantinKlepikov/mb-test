import math
from decimal import Decimal
from abc import ABC, abstractmethod


class BaseFigure(ABC):
    """_summary_

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def __init__(self, shape: dict[str, float]) -> None:
        ...

    @abstractmethod
    def area(self) -> None:
        ...


class Circle(BaseFigure):
    """Circle figure
    """
    def __init__(self, shape: dict[str, float]) -> None:
        """
        Args:
            shape dict[str, float]: shapes of circle. Must include 'radius' key

        Raises:
            ValueError: nonpositive radius
            KeyValueError: radius not define
        """
        if shape['radius'] <= 0:
            raise ValueError('Radius must be a positive float')
        self.shape = shape

    def area(self) -> float:
        """Area o circle

        Returns:
            float: area
        """

        return math.pi * (self.shape['radius']**2)


class Triangle(BaseFigure):
    """Triangle
    """
    def __init__(self, shape: dict[str, float]) -> None:
        """
        Args:
            shape dict[str, float]: shapes of circle. Must 3 side key, like `a`, `b`, `c`

        Raises:
            ValueError: nonpositive side value
        """
        if len(shape) != 3:
            raise ValueError('Triangle musrt have 3 sides.')
        if not all([True if i > 0 else False for i in shape.values()]):
            raise ValueError(
                'All sides of triangle must have a positive float value.'
                    )
        self.shape = shape

    def area(self) -> float:
        """Area o triangle

        Returns:
            float: area
        """
        v = self.shape.values()
        s = sum(v) / 2
        return (s*(s-v[0])*(s-v[1])*(s-v[2])) ** 0.5

    def is_right(self) -> bool:
        """Is triangle right side

        Returns:
            bool
        """
        v = self.shape.values()
        m = Decimal(max(v)) ** 2
        o = sum([Decimal(i) ** 2 for i in v if i != m])
        return True if m == o else False

