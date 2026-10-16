import unittest

from solution import (
    contact_search,
)


class Exercise54RequiredTests(unittest.TestCase):

    def test_contact_search_1(
        self,
    ) -> None:
        value_0 = [{'name': 'Ada', 'phone': '123'}]
        value_1 = 'Ada'
        expected_result = {'name': 'Ada', 'phone': '123'}

        actual_result = contact_search(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
