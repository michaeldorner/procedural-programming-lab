import unittest

from solution import minimum_of_three


class Exercise09RequiredTests(unittest.TestCase):

    def test_minimum_is_second_value(
        self,
    ) -> None:
        a: int = 3
        b: int = 1
        c: int = 2
        expected_result: int = 1

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_minimum_is_first_value(
        self,
    ) -> None:
        a: int = 1
        b: int = 2
        c: int = 3
        expected_result: int = 1

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_minimum_is_third_value(
        self,
    ) -> None:
        a: int = 3
        b: int = 2
        c: int = 1
        expected_result: int = 1

        actual_result: int = minimum_of_three(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
