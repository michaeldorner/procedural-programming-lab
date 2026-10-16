import unittest

from solution import is_even


class Exercise06RequiredTests(unittest.TestCase):

    def test_even_number(
        self,
    ) -> None:
        number: int = 4
        expected_result: bool = True

        actual_result: bool = is_even(
            number,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_odd_number(
        self,
    ) -> None:
        number: int = 5
        expected_result: bool = False

        actual_result: bool = is_even(
            number,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
