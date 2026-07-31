#!/usr/bin/python3
"""Unit tests for Base CSV methods."""
import unittest
import os
from models.rectangle import Rectangle
from models.square import Square


class TestBaseSaveToFileCSV(unittest.TestCase):
    """Tests for Base.save_to_file_csv."""

    def tearDown(self):
        for fname in ("Rectangle.csv", "Square.csv"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_save_rectangles_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.csv"))

    def test_save_none_csv(self):
        Rectangle.save_to_file_csv(None)
        with open("Rectangle.csv", "r") as f:
            self.assertEqual(f.read(), "")

    def test_save_squares_csv(self):
        Square.save_to_file_csv([Square(5), Square(7, 9, 1)])
        self.assertTrue(os.path.exists("Square.csv"))


class TestBaseLoadFromFileCSV(unittest.TestCase):
    """Tests for Base.load_from_file_csv."""

    def tearDown(self):
        for fname in ("Rectangle.csv", "Square.csv"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_no_file_returns_empty_list_csv(self):
        self.assertEqual(Rectangle.load_from_file_csv(), [])

    def test_load_rectangles_csv(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file_csv([r1, r2])
        loaded = Rectangle.load_from_file_csv()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_load_squares_csv(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file_csv([s1, s2])
        loaded = Square.load_from_file_csv()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())

    def test_load_returns_correct_type_csv(self):
        Rectangle.save_to_file_csv([Rectangle(1, 1)])
        loaded = Rectangle.load_from_file_csv()
        self.assertIsInstance(loaded[0], Rectangle)


if __name__ == "__main__":
    unittest.main()
