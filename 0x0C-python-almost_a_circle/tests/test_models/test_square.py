#!/usr/bin/python3
"""
    Unittest for Base class
"""
import unittest
import sys
from io import StringIO
from models.square import Square
from models.square import __doc__ as module_doc
from models.rectangle import Rectangle
from models.base import Base


class TestSquare(unittest.TestCase):
    """Subclass of unittest.TestCase to test Square class functionality"""

    def setUp(self):
        """Redirect stdout to readable buffer to check output of
        methods relying on print function."""
        sys.stdout = StringIO()

    def tearDown(self):
        """Following test completion reassign true stdout file stream to
        sys.stdout so printing goes to the screen as before."""
        sys.stdout = sys.__stdout__

    def test_docstrings(self):
        """Test for existence of docstrings"""
        self.assertIsNotNone(module_doc)
        self.assertIsNotNone(Square.__doc__)
        self.assertIs(hasattr(Square, "__init__"), True)
        self.assertIsNotNone(Square.__init__.__doc__)
        self.assertIs(hasattr(Square, "size"), True)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIs(hasattr(Square, "__str__"), True)
        self.assertIsNotNone(Square.__str__.__doc__)
        self.assertIs(hasattr(Square, "update"), True)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIs(hasattr(Square, "to_dictionary"), True)
        self.assertIsNotNone(Square.to_dictionary.__doc__)


class TestSquareClass(unittest.TestCase):
    """Test Cases Class"""

    def setUp(self):
        """Set up"""
        self.inst = Square(2, 3, 4, 5)

    def tearDown(self):
        """ Tear Dowm"""
        del self.inst
        Base._Base__nb_objects = 0

    def test_to_dict(self):
        """ Tear Dowm"""
        r1 = self.inst.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(r1, exp)

    def test_to_dict_1(self):
        """ Tear Dowm"""
        r1 = self.inst.to_dictionary()
        exp = {'x': 3, 'y': 4, 'id': 5, 'size': 2}
        self.assertEqual(type(r1).__name__, type(exp).__name__)

    def test_area(self):
        """ Test Area"""
        self.assertEqual(self.inst.area(), 4)

    def test_get_set_size(self):
        """ Test Area"""
        self.inst.size = 30
        self.assertEqual(str(self.inst), "[Square] (5) 3/4 - 30")

    def test_get_set_size_e(self):
        """ Test Area"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.size = "Fault"

    def out_c(self, x=None):
        """ Out std"""
        t = sys.stdout
        sys.stdout = StringIO()
        if x is None:
            self.inst.display()
        else:
            x.display()
        o = sys.stdout.getvalue()
        sys.stdout.close()
        sys.stdout = t
        return o

    def test_display(self):
        """ Test display"""
        display = "\n\n\n\n   ##\n   ##\n"
        o = self.out_c()
        self.assertEqual(o, display)

    def test_display_1(self):
        """ Test display"""
        r1 = Rectangle(4, 6)
        display = "####\n####\n####\n####\n####\n####\n"
        o = self.out_c(r1)
        self.assertEqual(o, display)

    def test_str(self):
        """ Test display"""
        self.assertEqual(str(self.inst), "[Square] (5) 3/4 - 2")

    def test_update_att(self):
        """ Test display"""
        self.inst.update(89)
        self.assertEqual(str(self.inst), "[Square] (89) 3/4 - 2")

    def test_update_dic(self):
        self.inst.update(x=6, y=3, size=7)
        self.assertEqual(str(self.inst), "[Square] (5) 6/3 - 7")

    def test_id(self):
        """ Test id"""
        self.assertEqual(self.inst.id, 5)

    def test_id_1(self):
        """ Test id 1"""
        self.inst.id = 0
        inst1 = Rectangle(1, 2)
        inst2 = Rectangle(2, 1)
        inst3 = Rectangle(1, 2, 3, 4)
        self.assertEqual(inst3.id, 3)

    def test_width(self):
        """ test width"""
        self.assertEqual(self.inst.width, 2)

    def test_height(self):
        """ test height"""
        self.assertEqual(self.inst.height, 2)

    def test_x(self):
        """ test x"""
        self.assertEqual(self.inst.x, 3)

    def test_y(self):
        """ test y"""
        self.assertEqual(self.inst.y, 4)

    def test_raise_width(self):
        """ test raise width"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.inst.width = "Fault"

    def test_raise_height(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            self.inst.height = "Fault"

    def test_raise_x(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            self.inst.x = "Fault"

    def test_raise_y(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            self.inst.y = "Fault"

    def test_raise_width_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.inst.width = 0

    def test_raise_height_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            self.inst.height = 0

    def test_raise_x_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            self.inst.x = -1

    def test_raise_y_1(self):
        """ test raise heigt"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            self.inst.y = -1


class TestSquareSize(unittest.TestCase):
    """Unittests for testing size initialization of the Square class."""

    def test_None_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(None)

    def test_str_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid")

    def test_float_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(5.5)

    def test_complex_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(complex(5))

    def test_dict_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({"a": 1, "b": 2}, 2)

    def test_bool_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 2, 3)

    def test_list_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])

    def test_set_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3}, 2)

    def test_tuple_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3), 2, 3)

    def test_frozenset_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(frozenset({1, 2, 3, 1}))

    def test_range_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(range(5))

    def test_bytes_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(b'Python')

    def test_bytearray_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(bytearray(b'abcdefg'))

    def test_memoryview_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(memoryview(b'abcdefg'))

    def test_inf_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('inf'))

    def test_nan_size(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(float('nan'))

    # Test size values
    def test_negative_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1, 2)

    def test_zero_size(self):
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 2)


class TestSquareX(unittest.TestCase):
    """Unittests for testing initialization of Square x attribute."""

    def test_None_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, None)

    def test_str_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid")

    def test_float_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 5.5)

    def test_complex_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, complex(5))

    def test_dict_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {"a": 1, "b": 2}, 2)

    def test_bool_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True)

    def test_list_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3])

    def test_set_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3})

    def test_tuple_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3))

    def test_frozenset_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, frozenset({1, 2, 3, 1}))

    def test_range_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, range(5))

    def test_bytes_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, b'Python')

    def test_bytearray_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, bytearray(b'abcdefg'))

    def test_memoryview_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, memoryview(b'abcedfg'))

    def test_inf_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('inf'), 2)

    def test_nan_x(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, float('nan'), 2)

    def test_negative_x(self):
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(5, -1, 0)


class TestSquareY(unittest.TestCase):
    """Unittests for testing initialization of Square y attribute."""

    def test_None_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, None)

    def test_str_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "invalid")

    def test_float_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, 5.5)

    def test_complex_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, complex(5))

    def test_dict_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {"a": 1, "b": 2})

    def test_list_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])

    def test_set_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})

    def test_tuple_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))

    def test_frozenset_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, frozenset({1, 2, 3, 1}))

    def test_range_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, range(5))

    def test_bytes_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, b'Python')

    def test_bytearray_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, bytearray(b'abcdefg'))

    def test_memoryview_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 3, memoryview(b'abcedfg'))

    def test_inf_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('inf'))

    def test_nan_y(self):
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, float('nan'))

    def test_negative_y(self):
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(3, 0, -1)


class TestSquareOrderOfInitialization(unittest.TestCase):
    """Unittests for testing order of Square attribute initialization."""

    def test_size_before_x(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", "invalid x")

    def test_size_before_y(self):
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("invalid size", 1, "invalid y")

    def test_x_before_y(self):
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "invalid x", "invalid y")


if __name__ == "__main__":
    unittest.main()
