import unittest

from solution import (
    min_max,
)


class Exercise27RequiredTests(unittest.TestCase):

    def test_min_max_1(
        self,
    ) -> None:
        value_0 = [3, 1, 4]
        expected_result = (1, 4)

        actual_result = min_max(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
