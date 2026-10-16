import unittest

from solution import (
    count_first_quadrant,
)


class Exercise50BonusTests(unittest.TestCase):

    def test_count_first_quadrant_1(
        self,
    ) -> None:
        value_0 = []
        expected_result = 0

        actual_result = count_first_quadrant(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
