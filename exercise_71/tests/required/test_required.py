import unittest

from solution import (
    library_search,
)


class Exercise71RequiredTests(unittest.TestCase):

    def test_library_search_1(
        self,
    ) -> None:
        value_0 = [{'title': 'Dune', 'author': 'Frank Herbert'}]
        value_1 = 'Dune'
        expected_result = {'title': 'Dune', 'author': 'Frank Herbert'}

        actual_result = library_search(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
