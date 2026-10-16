import unittest

from datetime import time

from solution import (
    is_working_hour,
)


class Exercise65RequiredTests(unittest.TestCase):

    def test_is_working_hour_1(
        self,
    ) -> None:
        value_0 = time(10, 0)
        expected_result = True

        actual_result = is_working_hour(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_is_working_hour_2(
        self,
    ) -> None:
        value_0 = time(18, 0)
        expected_result = False

        actual_result = is_working_hour(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
