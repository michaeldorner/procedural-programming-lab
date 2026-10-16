import unittest

from datetime import time

from solution import (
    minutes_between,
)


class Exercise62BonusTests(unittest.TestCase):

    def test_minutes_between_1(
        self,
    ) -> None:
        value_0 = time(23, 30)
        value_1 = time(0, 30)
        expected_result = 60

        actual_result = minutes_between(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
