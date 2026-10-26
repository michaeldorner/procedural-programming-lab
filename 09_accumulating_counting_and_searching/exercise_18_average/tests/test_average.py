import unittest

from solution import (
    average,
)


class ListAverageCalculationTests(unittest.TestCase):

    def test_whole_number_average(
        self,
    ) -> None:
        samples: list[float] = [1.0, 2.0, 3.0]
        expected_average: float = 2.0

        actual_average: float = average(
            samples,
        )

        self.assertAlmostEqual(
            actual_average,
            expected_average,
        )

    def test_fractional_average(
        self,
    ) -> None:
        samples: list[float] = [2.5, 3.5]
        expected_average: float = 3.0

        actual_average: float = average(
            samples,
        )

        self.assertAlmostEqual(
            actual_average,
            expected_average,
        )


if __name__ == "__main__":
    unittest.main()
