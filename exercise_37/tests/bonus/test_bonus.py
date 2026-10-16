import unittest

from solution import (
    lookup_phone,
)


class Exercise37BonusTests(unittest.TestCase):

    def test_lookup_phone_1(
        self,
    ) -> None:
        value_0 = {'Ada': '123'}
        value_1 = 'Alan'
        expected_result = ''

        actual_result = lookup_phone(
            value_0,
            value_1,
        )

        self.assertEqual(
            actual_result,
            expected_result,
        )


if __name__ == "__main__":
    unittest.main()
