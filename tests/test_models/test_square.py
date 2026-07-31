#!/usr/bin/python3
"""Unit tests for the Square class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square


class TestSquareInit(unittest.TestCase):
    """Tests for Square instantiation."""

    def test_is_rectangle_instance(self):
        self.assertIsInstance(Square(5), Rectangle)

    def test_width_equals_height(self):
        s = Square(5)
        self.assertEqual(s.width, s.height)
        self.assertEqual(s.width, 5)

    def test_default_x_y(self):
        s = Square(5)
        self.assertEqual((s.x, s.y), (0, 0))

    def test_custom_x_y(self):
        s = Square(3, 1, 3)
        self.assertEqual((s.x, s.y), (1, 3))

    def test_id_assigned(self):
        s = Square(5, 0, 0, 99)
        self.assertEqual(s.id, 99)

    def test_no_extra_attributes(self):
        s = Square(5)
        self.assertEqual(
            set(vars(s).keys()),
            {"_Rectangle__width", "_Rectangle__height",
             "_Rectangle__x", "_Rectangle__y", "id"})


class TestSquareValidation(unittest.TestCase):
    """Tests that Square inherits Rectangle's validation."""

    def test_size_not_int(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("5")

    def test_size_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)

    def test_size_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5)

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1)

    def test_y_not_int(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(5, 0, "1")


class TestSquareArea(unittest.TestCase):
    """Tests for Square.area (inherited from Rectangle)."""

    def test_area(self):
        self.assertEqual(Square(5).area(), 25)

    def test_area_other(self):
        self.assertEqual(Square(2, 2).area(), 4)


class TestSquareDisplay(unittest.TestCase):
    """Tests for Square.display (inherited from Rectangle)."""

    def test_display_basic(self):
        s = Square(5)
        expected = "#####\n" * 5
        with patch("sys.stdout", new=StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), expected)

    def test_display_with_offset(self):
        s = Square(3, 1, 3)
        expected = "\n\n\n ###\n ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as out:
            s.display()
            self.assertEqual(out.getvalue(), expected)


class TestSquareStr(unittest.TestCase):
    """Tests for Square.__str__."""

    def test_str_format(self):
        s = Square(5, 0, 0, 1)
        self.assertEqual(str(s), "[Square] (1) 0/0 - 5")

    def test_str_with_offset(self):
        s = Square(2, 2, 0, 2)
        self.assertEqual(str(s), "[Square] (2) 2/0 - 2")


class TestSquareSizeProperty(unittest.TestCase):
    """Tests for Square.size getter/setter."""

    def test_getter(self):
        s = Square(5)
        self.assertEqual(s.size, 5)

    def test_setter_updates_width_height(self):
        s = Square(5)
        s.size = 10
        self.assertEqual(s.width, 10)
        self.assertEqual(s.height, 10)

    def test_setter_validation_type(self):
        s = Square(5)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s.size = "9"

    def test_setter_validation_value(self):
        s = Square(5)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s.size = -1


class TestSquareUpdateArgs(unittest.TestCase):
    """Tests for Square.update with *args."""

    def setUp(self):
        self.s = Square(5)

    def test_update_id_only(self):
        self.s.update(10)
        self.assertEqual(str(self.s), "[Square] (10) 0/0 - 5")

    def test_update_id_size(self):
        self.s.update(1, 2)
        self.assertEqual(str(self.s), "[Square] (1) 0/0 - 2")

    def test_update_full(self):
        self.s.update(1, 2, 3, 4)
        self.assertEqual(str(self.s), "[Square] (1) 3/4 - 2")

    def test_update_no_args(self):
        original = str(self.s)
        self.s.update()
        self.assertEqual(str(self.s), original)


class TestSquareUpdateKwargs(unittest.TestCase):
    """Tests for Square.update with **kwargs."""

    def setUp(self):
        self.s = Square(5)

    def test_update_kwargs(self):
        self.s.update(size=7, id=89, y=1)
        self.assertEqual(str(self.s), "[Square] (89) 0/1 - 7")

    def test_kwargs_skipped_if_args(self):
        self.s.update(50, x=999)
        self.assertNotEqual(self.s.x, 999)


class TestSquareToDictionary(unittest.TestCase):
    """Tests for Square.to_dictionary."""

    def test_keys(self):
        s = Square(10, 2, 1)
        d = s.to_dictionary()
        self.assertEqual(set(d.keys()), {"id", "size", "x", "y"})

    def test_values(self):
        s = Square(10, 2, 1, 5)
        self.assertEqual(
            s.to_dictionary(), {"id": 5, "size": 10, "x": 2, "y": 1})

    def test_round_trip_via_update(self):
        s1 = Square(10, 2, 1)
        s2 = Square(1, 1)
        s2.update(**s1.to_dictionary())
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())


if __name__ == "__main__":
    unittest.main()
