import unittest

from solution import (
    count_occurrences,
)


class Exercise21RequiredTests(unittest.TestCase):

    def test_count_occurrences_1(
        self,
    ) -> None:
        value_0 = [1, 2, 2, 3]
        value_1 = 2
        expected_result = 2

        actual_result = count_occurrences(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
