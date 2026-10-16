import unittest

from solution import (
    add_todo,
)


class Exercise69RequiredTests(unittest.TestCase):

    def test_add_todo_1(
        self,
    ) -> None:
        value_0 = ['learn']
        value_1 = 'test'
        expected_result = ['learn', 'test']

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
