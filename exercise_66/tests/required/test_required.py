import unittest

from datetime import datetime

from solution import (
    appointments_overlap,
)


class Exercise66RequiredTests(unittest.TestCase):

    def test_appointments_overlap_1(
        self,
    ) -> None:
        value_0 = datetime(2026, 1, 1, 9, 0)
        value_1 = datetime(2026, 1, 1, 10, 0)
        value_2 = datetime(2026, 1, 1, 9, 30)
        value_3 = datetime(2026, 1, 1, 10, 30)
        expected_result = True

        actual_result = appointments_overlap(
            value_0,
            value_1,
            value_2,
            value_3,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
