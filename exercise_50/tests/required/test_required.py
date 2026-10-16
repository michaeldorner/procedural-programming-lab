import unittest

from solution import (
    count_first_quadrant,
)


class Exercise50RequiredTests(unittest.TestCase):

    def test_count_first_quadrant_1(
        self,
    ) -> None:
        value_0 = [(1.0, 1.0), (-1.0, 1.0), (2.0, 3.0)]
        expected_result = 2

        actual_result = count_first_quadrant(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
