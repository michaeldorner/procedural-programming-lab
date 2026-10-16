import unittest

from solution import (
    maximum,
)


class Exercise19RequiredTests(unittest.TestCase):

    def test_maximum_1(
        self,
    ) -> None:
        value_0 = [1, 5, 3]
        expected_result = 5

        actual_result = maximum(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
