#!/usr/bin/python3
"""Unit tests for the Rectangle class."""
import unittest
from io import StringIO
from unittest.mock import patch
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleInit(unittest.TestCase):
    """Tests for Rectangle instantiation."""

    def test_is_base_instance(self):
        r = Rectangle(10, 2)
        self.assertIsInstance(r, Base)

    def test_width_height(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 2)

    def test_default_x_y(self):
        r = Rectangle(10, 2)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    def test_custom_x_y(self):
        r = Rectangle(10, 2, 3, 4)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)

    def test_id_assigned(self):
        r = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r.id, 12)

    def test_id_auto(self):
        r1 = Rectangle(10, 2)
        r2 = Rectangle(10, 2)
        self.assertEqual(r2.id, r1.id + 1)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 0, 0, 1, 2)

    def test_missing_args(self):
        with self.assertRaises(TypeError):
            Rectangle(10)


class TestRectangleValidation(unittest.TestCase):
    """Tests for Rectangle attribute validation."""

    def test_width_not_int_str(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("10", 2)

    def test_height_not_int_str_matches_official_example(self):
        # Matches the official task example: Rectangle(10, "2")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_width_not_int_float(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(10.5, 2)

    def test_width_not_int_none(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(None, 2)

    def test_width_zero(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 2)

    def test_width_negative(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-10, 2)

    def test_height_not_int(self):
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(10, "2")

    def test_height_zero(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, 0)

    def test_height_negative(self):
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(10, -2)

    def test_x_not_int(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(10, 2, {})

    def test_x_negative(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(10, 2, -3)

    def test_x_zero_ok(self):
        r = Rectangle(10, 2, 0)
        self.assertEqual(r.x, 0)

    def test_y_not_int(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(10, 2, 3, "1")

    def test_y_negative(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(10, 2, 3, -1)

    def test_setter_width(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -10

    def test_setter_x(self):
        r = Rectangle(10, 2)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.x = {}

    def test_bool_accepted_as_int_subclass(self):
        # bool is a subclass of int in Python; the spec doesn't require
        # rejecting it, so True/False behave as 1/0 here.
        r = Rectangle(True, 2)
        self.assertEqual(r.width, True)


class TestRectangleArea(unittest.TestCase):
    """Tests for Rectangle.area."""

    def test_area_basic(self):
        self.assertEqual(Rectangle(3, 2).area(), 6)

    def test_area_2(self):
        self.assertEqual(Rectangle(2, 10).area(), 20)

    def test_area_with_id(self):
        self.assertEqual(Rectangle(8, 7, 0, 0, 12).area(), 56)

    def test_area_no_args(self):
        r = Rectangle(2, 3)
        with self.assertRaises(TypeError):
            r.area(1)


class TestRectangleDisplay(unittest.TestCase):
    """Tests for Rectangle.display."""

    def test_display_basic(self):
        r = Rectangle(4, 6)
        expected = "####\n" * 6
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)

    def test_display_small(self):
        r = Rectangle(2, 2)
        expected = "##\n##\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)

    def test_display_with_x_y(self):
        r = Rectangle(2, 3, 2, 2)
        expected = "\n\n  ##\n  ##\n  ##\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)

    def test_display_x_only(self):
        r = Rectangle(3, 2, 1, 0)
        expected = " ###\n ###\n"
        with patch("sys.stdout", new=StringIO()) as out:
            r.display()
            self.assertEqual(out.getvalue(), expected)


class TestRectangleStr(unittest.TestCase):
    """Tests for Rectangle.__str__."""

    def test_str_with_id(self):
        r = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r), "[Rectangle] (12) 2/1 - 4/6")

    def test_str_auto_id(self):
        r = Rectangle(5, 5, 1)
        self.assertEqual(str(r), "[Rectangle] ({}) 1/0 - 5/5".format(r.id))


class TestRectangleUpdateArgs(unittest.TestCase):
    """Tests for Rectangle.update with *args."""

    def setUp(self):
        self.r = Rectangle(10, 10, 10, 10)

    def test_update_id(self):
        self.r.update(89)
        self.assertEqual(self.r.id, 89)

    def test_update_id_width(self):
        self.r.update(89, 2)
        self.assertEqual((self.r.id, self.r.width), (89, 2))

    def test_update_full(self):
        self.r.update(89, 2, 3, 4, 5)
        self.assertEqual(str(self.r), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_no_args(self):
        original = str(self.r)
        self.r.update()
        self.assertEqual(str(self.r), original)


class TestRectangleUpdateKwargs(unittest.TestCase):
    """Tests for Rectangle.update with **kwargs."""

    def setUp(self):
        self.r = Rectangle(10, 10, 10, 10)

    def test_update_kwargs(self):
        self.r.update(y=1, width=2, x=3, id=89)
        self.assertEqual(str(self.r), "[Rectangle] (89) 3/1 - 2/10")

    def test_kwargs_skipped_if_args(self):
        self.r.update(50, x=999)
        self.assertEqual(self.r.id, 50)
        self.assertNotEqual(self.r.x, 999)

    def test_update_unknown_kwarg_sets_attribute(self):
        r = Rectangle(1, 1)
        r.update(foo=1)
        self.assertEqual(r.foo, 1)


class TestRectangleToDictionary(unittest.TestCase):
    """Tests for Rectangle.to_dictionary."""

    def test_keys(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        self.assertEqual(
            set(d.keys()), {"id", "width", "height", "x", "y"})

    def test_values(self):
        r = Rectangle(10, 2, 1, 9, 5)
        d = r.to_dictionary()
        self.assertEqual(d, {
            "id": 5, "width": 10, "height": 2, "x": 1, "y": 9})

    def test_returns_dict(self):
        self.assertIsInstance(Rectangle(1, 1).to_dictionary(), dict)

    def test_independent_copy(self):
        r = Rectangle(10, 2, 1, 9)
        d = r.to_dictionary()
        d["width"] = 999
        self.assertEqual(r.width, 10)

    def test_round_trip_via_update(self):
        r1 = Rectangle(10, 2, 1, 9)
        r2 = Rectangle(1, 1)
        r2.update(**r1.to_dictionary())
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())


if __name__ == "__main__":
    unittest.main()
