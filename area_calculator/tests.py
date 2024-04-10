import unittest
from math import pi, sqrt

from area_calculator.figures import Circle, Triangle
from area_calculator.utils import calc_area

RADIUS = 3
SIDE1 = 3
SIDE2 = 4
SIDE3 = 5


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(RADIUS)

    def test_area_method(self):
        self.assertEqual(self.circle.area(), round(pi * RADIUS ** 2, 2))

    def test_radius_getter(self):
        self.assertEqual(self.circle.radius, RADIUS)

    def test_radius_setter(self):
        self.circle.radius = 5
        self.assertEqual(self.circle.radius, 5)

    def test_radius_setter_invalid_data_type(self):
        with self.assertRaises(ValueError):
            self.circle.radius = "some string"

    def test_radius_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            self.circle.radius = -2


class TestTriangleInit(unittest.TestCase):
    def test_init_with_one_argument(self):
        triangle = Triangle(SIDE1)
        self.assertEqual(triangle.side1, SIDE1)
        self.assertEqual(triangle.side2, SIDE1)
        self.assertEqual(triangle.side3, SIDE1)

    def test_init_with_three_arguments(self):
        triangle = Triangle(SIDE1, SIDE2, SIDE3)
        self.assertEqual(triangle.side1, SIDE1)
        self.assertEqual(triangle.side2, SIDE2)
        self.assertEqual(triangle.side3, SIDE3)

    def test_init_with_two_arguments(self):
        with self.assertRaises(ValueError):
            triangle = Triangle(SIDE1, SIDE2)


class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(SIDE1, SIDE2, SIDE3)

    def test_area_method(self):
        p = (SIDE1 + SIDE2 + SIDE3) / 2
        expected = round(sqrt(p * (p - SIDE1) * (p - SIDE2) * (p - SIDE3)), 2)
        self.assertEqual(self.triangle.area(), expected)

    def test_side_getter(self):
        self.assertEqual(self.triangle.side1, SIDE1)
        self.assertEqual(self.triangle.side2, SIDE2)
        self.assertEqual(self.triangle.side3, SIDE3)

    def test_side_setter(self):
        self.triangle.side1 = 6
        self.assertEqual(self.triangle.side1, 6)

    def test_side_setter_invalid_data_type(self):
        with self.assertRaises(ValueError):
            self.triangle.side1 = "some string"

    def test_side_setter_invalid_value(self):
        with self.assertRaises(ValueError):
            self.triangle.side1 = -5

    def test_is_right_triangle_true(self):
        self.assertEqual(self.triangle.is_right_triangle, True)

    def test_is_right_triangle_false(self):
        self.triangle.side3 = 6
        self.assertEqual(self.triangle.is_right_triangle, False)


class TestCalcAreaFunc(unittest.TestCase):
    def test_for_circle(self):
        circle = Circle(RADIUS)
        self.assertEqual(calc_area(circle), round(pi * RADIUS ** 2, 2))

    def test_for_triangle(self):
        triangle = Triangle(SIDE1, SIDE2, SIDE3)
        p = (SIDE1 + SIDE2 + SIDE3) / 2
        expected = round(sqrt(p * (p - SIDE1) * (p - SIDE2) * (p - SIDE3)), 2)
        self.assertEqual(calc_area(triangle), expected)

    def test_for_unsupported_object_type(self):
        obj = [1, 2, 3]
        with self.assertRaises(ValueError):
            calc_area(obj)


if __name__ == "__main__":
    unittest.main()
