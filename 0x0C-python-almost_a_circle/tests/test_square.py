#!/usr/bin/python3
"""Unittests for Rectangle class"""
import csv
import io
import json
import sys
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangleClass(unittest.TestCase):
    def test_init_empty(self):
        """Initialize with no arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle()

    def test_init_oneparam(self):
        """Initialize with one argument"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(1)

    def test_init_wh(self):
        """Initialize width and height"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)
        r2 = Rectangle(2, 3)
        self.assertEqual(r2.id - r1.id, 1)

    def test_init_whxy(self):
        """Initialize width, height, x, and y"""
        r1 = Rectangle(10, 2, 3, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_init_all(self):
        """Initialize width, height, x, y, and id"""
        r1 = Rectangle(10, 2, 3, 3, 98)
        self.assertEqual(r1.id, 98)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 3)
        self.assertEqual(r1.y, 3)

    def test_init_toomany(self):
        """Initialize with too many arguments"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(10, 2, 3, 4, 5, 6)

    def test_init_no_wh(self):
        """Try to initialize without width and height"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(x=3, y=3)

    def test_width_type_valid(self):
        """Initialize with invalid type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle("10", 0)
        with self.assertRaises(TypeError):
            r1 = Rectangle((10, ), 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle([10], 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle({10: 2}, 2)

    def test_height_type_valid(self):
        """Initialize with invalid type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, "10")
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, (10, ))
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, [10])
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, {10: 2})

    def test_x_type_valid(self):
        """Initialize with invalid type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, "10", 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, "10", 0)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, (10, ), 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, [10], 2)
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, {10: 2}, 2)

    def test_y_type_valid(self):
        """Initialize with invalid type"""
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, "10")
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, (10, ))
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, [10])
        with self.assertRaises(TypeError):
            r1 = Rectangle(2, 3, 2, {10: 2})

    def test_width_0(self):
        """Initialize width with invalid value (0)"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(0, 3)

    def test_height_0(self):
        """Initialize height with invalid value (0)"""
        with self.assertRaises(ValueError):
            r1 = Rectangle(2, 0)

    def test_xy_0(self):
        """Initialize x and y with valid value 0"""
        r1 = Rectangle(2, 3, 0, 0)
        self.assertEqual(r1.width, 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_negative(self):
        """Initialize with negative value (invalid)"""
        with self.assertRaises(ValueError):
            Rectangle(10, -2)
        with self.assertRaises(ValueError):
            Rectangle(-10, 2)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, -1, 3)
        with self.assertRaises(ValueError):
            Rectangle(10, 2, 1, -3)

    def test_area(self):
        """Test area function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)
        r1.width = 2
        r1.height = 10
        self.assertEqual(r1.area(), 20)
        r2 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r2.area(), 56)

    def test_display(self):
        """Test display function"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(4, 6)
        r1.display()
        r1 = Rectangle(2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(),
                         '####\n####\n####\n####\n####\n####\n##\n##\n')

    def test_str(self):
        """Test str function"""
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")

    def test_print(self):
        """Test str function with print"""
        captured = io.StringIO()
        sys.stdout = captured
        r2 = Rectangle(5, 5, 1, id=1)
        print(r2)
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "[Rectangle] (1) 1/0 - 5/5\n")

    def test_display_xy(self):
        """Test display with x and y position"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n\n  ##\n  ##\n  ##\n")

    def test_display_0y(self):
        """Test display with x=0 and y position"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(3, 2, 0, 1)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), "\n###\n###\n")


    def test_display_x0(self):
        """Test display with x position and y=0"""
        captured = io.StringIO()
        sys.stdout = captured
        r1 = Rectangle(3, 2, 1, 0)
        r1.display()
        sys.stdout = sys.__stdout__
        self.assertEqual(captured.getvalue(), " ###\n ###\n")

    def test_update1(self):
        """Test update first attribute (id)"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")

    def test_update2(self):
        """Test update first two attributes (id, width)"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")

    def test_update3(self):
        """Test update id, width, height"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")

    def test_update4(self):
        """Test update id, width, height, x"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")

    def test_update5(self):
        """Test update id, width, height, x, y"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_toomany(self):
        """Test update with too many arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(89, 2, 3, 4, 5, 6)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")

    def test_update_invalid_value(self):
        """Test update with invalid value"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        with self.assertRaises(ValueError):
            r1.update(89, -1)

    def test_update_invalid_type(self):
        """Test update with invalid type"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        r1 = Rectangle(10, 10, 10, 10, 1)
        selfrguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(width=1, x=2)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 2/10 - 1/10")

    def test_update_kwargs3.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        with self.assertRaises(TypeError):
            r1.update(89, "1")

    def test_update_kwargs1(self):
        """Test update with one keyword argument"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(height=1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/1")

    def test_update_kwargs2(self):
        """Test update with two keyword a(self):
        """Test update with three keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(y=1, id=2, width=9)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 10/1 - 9/10")

    def test_update_kwargs4(self):
        """Test update with four keyword arguments"""
        r1 = Rectangle(10, 10, 10, 10, 1)
        self.assertEqual(r1.__str__(), "[Rectangle] (1) 10/10 - 10/10")
        r1.update(y=1, id=2, x=8, height=7)
        self.assertEqual(r1.__str__(), "[Rectangle] (2) 8/1 - 10/7")
