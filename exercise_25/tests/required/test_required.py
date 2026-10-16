import unittest

from solution import (
    midpoint,
)


class Exercise25RequiredTests(unittest.TestCase):

    def test_midpoint_1(
        self,
    ) -> None:
        value_0 = (0.0, 0.0)
        value_1 = (2.0, 4.0)
        expected_result = (1.0, 2.0)

        actual_result = midpoint(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
