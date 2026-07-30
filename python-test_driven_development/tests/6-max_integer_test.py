#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Tests for the max_integer function."""

    def test_ordered_list(self):
        """Test with an ordered list."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test with an unordered list."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_default_argument(self):
        """Test with no arguments (default empty list)."""
        self.assertEqual(max_integer(), None)

    def test_single_element(self):
        """Test with a single element list."""
        self.assertEqual(max_integer([5]), 5)

    def test_negative_numbers(self):
        """Test with negative numbers."""
        self.assertEqual(max_integer([-1, -3, -4, -2]), -1)

    def test_all_same(self):
        """Test with all the same numbers."""
        self.assertEqual(max_integer([2, 2, 2, 2]), 2)

    def test_floats(self):
        """Test with float numbers."""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_max_at_start(self):
        """Test with max value at the start."""
        self.assertEqual(max_integer([10, 1, 2, 3]), 10)

    def test_max_at_end(self):
        """Test with max value at the end."""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)


if __name__ == '__main__':
    unittest.main()
