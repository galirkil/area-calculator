from abc import ABC, abstractmethod
from math import pi, sqrt


class Figure(ABC):
    """
    All classes for certain figures must be sublassed
    from this base class.
    """

    @abstractmethod
    def area(self) -> float:
        raise NotImplementedError("Method must be implemented in subclass!")


class FigureMeasurement:
    """
    Descriptor class for attributes that represent figure's measurements.

    Checks if attribute is of acceptable type and value.
    """

    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Only args of int or float type are accepted!")
        elif value <= 0:
            raise ValueError("Figure measurement must be positive!")
        else:
            instance.__dict__[self._name] = value


class Circle(Figure):
    """
    Class for circle figure.

    Takes one argument that represents the radius of circle in cm.
    """
    radius = FigureMeasurement()

    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"Circle with a radius of {self.radius} cm."

    def area(self) -> float:
        return round(pi * self.radius ** 2, 2)


class Triangle(Figure):
    """
    Class for triangle figure.

    Takes one or three arguments that represent lengths of sides of
    figure in cm. If only one argument passed, all sides will be equal
    to that argument's value.
    """
    side1 = FigureMeasurement()
    side2 = FigureMeasurement()
    side3 = FigureMeasurement()

    def __init__(self, *sides: int | float):
        if len(sides) == 1:
            self.side1 = self.side2 = self.side3 = sides[0]
        elif len(sides) == 3:
            self.side1, self.side2, self.side3 = sides
        else:
            raise ValueError(
                "Triangle requires either one or three side's lengths!"
            )

    def __str__(self):
        return f"Triangle with sides {self.side1} cm, {self.side2} cm, " \
               f"{self.side3} cm."

    def area(self) -> float:
        p = (self.side1 + self.side2 + self.side3) / 2
        return round(
            sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3)), 2
        )

    @property
    def is_right_triangle(self) -> bool:
        sides = sorted([self.side1, self.side2, self.side3])
        return sides[0] ** 2 + sides[1] ** 2 == sides[2] ** 2
