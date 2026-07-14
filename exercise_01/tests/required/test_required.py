import unittest

from solution import (
    rectangle_area,
    rectangle_perimeter,
)


class Exercise01RequiredTests(unittest.TestCase):

    def test_rectangle_area(self):
        self.assertEqual(
            rectangle_area(3.0, 4.0),
            12.0,
        )

    def test_rectangle_perimeter(self):
        self.assertEqual(
            rectangle_perimeter(3.0, 4.0),
            14.0,
        )


if __name__ == "__main__":
    unittest.main()
