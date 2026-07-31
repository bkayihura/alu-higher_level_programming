#!/usr/bin/python3
"""Unit tests for the Base class."""
import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """Tests for the Base class."""

    def test_id_public(self):
        b = Base(5)
        self.assertEqual(b.id, 5)

    def test_id_none_increments(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_id_none_default(self):
        b = Base()
        self.assertIsInstance(b.id, int)

    def test_id_negative(self):
        b = Base(-5)
        self.assertEqual(b.id, -5)

    def test_id_zero(self):
        b = Base(0)
        self.assertEqual(b.id, 0)

    def test_no_args(self):
        with self.assertRaises(TypeError):
            Base(1, 2)


class TestBaseToJSONString(unittest.TestCase):
    """Tests for Base.to_json_string."""

    def test_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_empty_list(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_list_of_dicts(self):
        list_dicts = [{"id": 1}, {"id": 2}]
        result = Base.to_json_string(list_dicts)
        self.assertEqual(json.loads(result), list_dicts)

    def test_returns_str(self):
        self.assertIsInstance(Base.to_json_string([{"id": 1}]), str)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.to_json_string([{"id": 1}], [{"id": 2}])


class TestBaseFromJSONString(unittest.TestCase):
    """Tests for Base.from_json_string."""

    def test_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_empty_string(self):
        self.assertEqual(Base.from_json_string(""), [])

    def test_valid_json(self):
        json_string = '[{"id": 1}, {"id": 2}]'
        self.assertEqual(
            Base.from_json_string(json_string), [{"id": 1}, {"id": 2}])

    def test_returns_list(self):
        self.assertIsInstance(Base.from_json_string("[]"), list)

    def test_round_trip(self):
        list_dicts = [{"id": 1, "width": 3}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(Base.from_json_string(json_string), list_dicts)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Base.from_json_string("[]", "[]")


class TestBaseSaveToFile(unittest.TestCase):
    """Tests for Base.save_to_file."""

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_save_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        self.assertTrue(os.path.exists("Rectangle.json"))
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
        self.assertEqual(len(content), 2)

    def test_save_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_empty_list(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as f:
            self.assertEqual(f.read(), "[]")

    def test_save_overwrites(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        Rectangle.save_to_file([Rectangle(2, 2), Rectangle(3, 3)])
        with open("Rectangle.json", "r") as f:
            content = json.load(f)
        self.assertEqual(len(content), 2)

    def test_save_squares(self):
        Square.save_to_file([Square(5), Square(7, 9, 1)])
        self.assertTrue(os.path.exists("Square.json"))

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file([], [])


class TestBaseCreate(unittest.TestCase):
    """Tests for Base.create."""

    def test_create_rectangle(self):
        r1 = Rectangle(3, 5, 1)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertIsNot(r1, r2)
        self.assertEqual(r1.to_dictionary(), r2.to_dictionary())

    def test_create_square(self):
        s1 = Square(5, 2, 3, 9)
        s1_dict = s1.to_dictionary()
        s2 = Square.create(**s1_dict)
        self.assertIsNot(s1, s2)
        self.assertEqual(s1.to_dictionary(), s2.to_dictionary())

    def test_create_returns_instance(self):
        r = Rectangle.create(id=89, width=1, height=1, x=0, y=0)
        self.assertIsInstance(r, Rectangle)


class TestBaseLoadFromFile(unittest.TestCase):
    """Tests for Base.load_from_file."""

    def tearDown(self):
        for fname in ("Rectangle.json", "Square.json"):
            if os.path.exists(fname):
                os.remove(fname)

    def test_no_file_returns_empty_list(self):
        self.assertEqual(Rectangle.load_from_file(), [])

    def test_load_rectangles(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
        loaded = Rectangle.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded[1].to_dictionary(), r2.to_dictionary())

    def test_load_squares(self):
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        Square.save_to_file([s1, s2])
        loaded = Square.load_from_file()
        self.assertEqual(len(loaded), 2)
        self.assertEqual(loaded[0].to_dictionary(), s1.to_dictionary())

    def test_load_returns_list_of_correct_type(self):
        Rectangle.save_to_file([Rectangle(1, 1)])
        loaded = Rectangle.load_from_file()
        self.assertIsInstance(loaded[0], Rectangle)

    def test_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(5)


if __name__ == "__main__":
    unittest.main()
