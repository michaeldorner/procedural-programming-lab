import unittest

from solution import (
    add_todo,
)


class TodoListTests(unittest.TestCase):

    def test_append_task_to_existing_list(
        self,
    ) -> None:
        initial_tasks: list[str] = ["learn"]
        new_task: str = "test"
        expected_tasks: list[str] = ["learn", "test"]

        actual_tasks: list[str] = add_todo(
            initial_tasks,
            new_task,
        )

        self.assertEqual(
            actual_tasks,
            expected_tasks,
        )

    def test_append_task_to_empty_list(
        self,
    ) -> None:
        initial_tasks: list[str] = []
        new_task: str = "start"
        expected_tasks: list[str] = ["start"]

        actual_tasks: list[str] = add_todo(
            initial_tasks,
            new_task,
        )

        self.assertEqual(
            actual_tasks,
            expected_tasks,
        )


if __name__ == "__main__":
    unittest.main()
