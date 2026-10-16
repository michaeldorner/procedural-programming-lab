import unittest

from solution import (
    common_elements,
)


class Exercise30RequiredTests(unittest.TestCase):

    def test_common_elements_1(
        self,
    ) -> None:
        value_0 = [1, 2, 3]
        value_1 = [2, 3, 4]
        expected_result = {2, 3}

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
