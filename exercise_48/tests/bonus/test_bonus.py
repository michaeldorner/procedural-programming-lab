import unittest

from solution import (
    normalize_text,
)


class Exercise48BonusTests(unittest.TestCase):

    def test_normalize_text_1(
        self,
    ) -> None:
        value_0 = 'PYTHON'
        expected_result = 'python'

        actual_result = normalize_text(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
