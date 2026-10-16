import unittest

from solution import (
    character_frequencies,
)


class Exercise35RequiredTests(unittest.TestCase):

    def test_character_frequencies_1(
        self,
    ) -> None:
        value_0 = 'aba'
        expected_result = {'a': 2, 'b': 1}

        actual_result = character_frequencies(
            value_0,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
