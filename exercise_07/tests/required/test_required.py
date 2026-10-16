import unittest

from solution import grade


class Exercise07RequiredTests(unittest.TestCase):

    def test_grade_a(
        self,
    ) -> None:
        score: int = 95
        expected_result: str = "A"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_b(
        self,
    ) -> None:
        score: int = 82
        expected_result: str = "B"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_grade_f(
        self,
    ) -> None:
        score: int = 58
        expected_result: str = "F"

        actual_result: str = grade(
            score,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
