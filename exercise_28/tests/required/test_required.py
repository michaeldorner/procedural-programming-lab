import unittest

from solution import (
    split_name,
)


class Exercise28RequiredTests(unittest.TestCase):

    def test_split_name_1(
        self,
    ) -> None:
        value_0 = 'Ada Lovelace'
        expected_result = ('Ada', 'Lovelace')

        actual_result = split_name(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
