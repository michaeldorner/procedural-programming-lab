import unittest

from solution import (
    contact_search,
)


class Exercise54BonusTests(unittest.TestCase):

    def test_contact_search_1(
        self,
    ) -> None:
        value_0 = [{'name': 'Ada', 'phone': '123'}]
        value_1 = 'Alan'
        expected_result = None

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
