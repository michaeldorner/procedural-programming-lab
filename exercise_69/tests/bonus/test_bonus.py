import unittest

from solution import (
    add_todo,
)


class Exercise69BonusTests(unittest.TestCase):

    def test_add_todo_1(
        self,
    ) -> None:
        value_0 = []
        value_1 = 'start'
        expected_result = ['start']

        actual_result = add_todo(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
