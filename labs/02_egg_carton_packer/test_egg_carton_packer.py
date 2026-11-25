"""Unit tests for egg_carton_packer."""

import unittest

from egg_carton_packer import full_cartons, loose_eggs, minimum_cartons_needed


class TestEggCartonPacker(unittest.TestCase):
    """Tests for carton packing helpers."""

    def test_full_and_loose(self) -> None:
        self.assertEqual(full_cartons(26, 12), 2)
        self.assertEqual(loose_eggs(26, 12), 2)
        self.assertEqual(full_cartons(24, 12), 2)
        self.assertEqual(loose_eggs(24, 12), 0)

    def test_minimum_cartons_needed(self) -> None:
        self.assertEqual(minimum_cartons_needed(0, 12), 0)
        self.assertEqual(minimum_cartons_needed(24, 12), 2)
        self.assertEqual(minimum_cartons_needed(25, 12), 3)

    def test_invalid_inputs_raise_value_error(self) -> None:
        for fn in (full_cartons, loose_eggs, minimum_cartons_needed):
            with self.assertRaises(ValueError):
                fn(-1, 12)
            with self.assertRaises(ValueError):
                fn(10, 0)
            with self.assertRaises(ValueError):
                fn(10, -6)
