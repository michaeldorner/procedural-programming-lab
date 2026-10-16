import unittest

from solution import (
    common_elements,
)


class Exercise30BonusTests(unittest.TestCase):

    def test_common_elements_1(
        self,
    ) -> None:
        value_0 = [1]
        value_1 = [2]
        expected_result = set()

        actual_result = common_elements(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
