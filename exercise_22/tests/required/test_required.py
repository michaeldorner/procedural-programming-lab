import unittest

from solution import (
    linear_search,
)


class Exercise22RequiredTests(unittest.TestCase):

    def test_linear_search_1(
        self,
    ) -> None:
        value_0 = [4, 5, 6]
        value_1 = 5
        expected_result = 1

        actual_result = linear_search(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
