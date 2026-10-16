import unittest

from solution import triangle_type


class Exercise10RequiredTests(unittest.TestCase):

    def test_equilateral_triangle(
        self,
    ) -> None:
        a: float = 3.0
        b: float = 3.0
        c: float = 3.0
        expected_result: str = "equilateral"

        actual_result: str = triangle_type(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_isosceles_triangle(
        self,
    ) -> None:
        a: float = 3.0
        b: float = 3.0
        c: float = 4.0
        expected_result: str = "isosceles"

        actual_result: str = triangle_type(
            a,
            b,
            c,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )

    def test_scalene_triangle(
        self,
    ) -> None:
        a: float = 3.0
        b: float = 4.0
        c: float = 5.0
        expected_result: str = "scalene"

        actual_result: str = triangle_type(
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
