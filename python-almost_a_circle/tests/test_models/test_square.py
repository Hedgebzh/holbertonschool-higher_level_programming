#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.square import Square


class TestSquare(unittest.TestCase):
  """Testing Square"""
  def test_instance(self):
      """test input size correct standard """
      s = Square(5)
      self.assertEqual(s.size, 5)
  def test_area(self):
      """testing area"""

      s = Square(5)
      self.assertEqual(s.area(), 25)

      s = Square(1, 2)
      self.assertEqual(s.area(), 1)
  def test_display(self):
      """test display()"""
      s = Square(5)
      with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
        s.display()

      assert mock_stdout.getvalue() == "#####\n#####\n#####\n#####\n#####\n"

      s = Square(1, 2)
      with mock.patch("sys.stdout", new=io.StringIO()) as mock_stdout:
        s.display()

      assert mock_stdout.getvalue() == "  #\n"
  def test_string(self):
      """Test str"""

      s = Square(1, 2)
      self.assertEqual(s.__str__(), '[Square] (11) 2/0 - 1')

class TestSquare_update_args(unittest.TestCase):
    """unittests for testing update function"""

    def test_update_zero_args(self):
      """Test update function with zero args"""
      s = Square(5, 5, 5, 5)
      s.update()
      self.assertEqual("[Square] (5) 5/5 - 5", str(s))

    def test_update_one_args(self):
      """Test update function with one args"""
      s = Square(5, 5, 5, 5)
      s.update(89)
      self.assertEqual("[Square] (89) 5/5 - 5", str(s))

    def test_update_two_args(self):
      """Test update function with two args"""
      s = Square(5, 5, 5, 5)
      s.update(89, 1)
      self.assertEqual("[Square] (89) 5/5 - 1", str(s))

    def test_update_three_args(self):
      """Test update function with three args"""
      s = Square(5, 5, 5, 5)
      s.update(89, 1, 2)
      self.assertEqual("[Square] (89) 2/5 - 1", str(s))

    def test_update_four_args(self):
      """Test update function with four args"""
      s = Square(5, 5, 5, 5)
      s.update(89, 1, 2, 3)
      self.assertEqual("[Square] (89) 2/3 - 1", str(s))




if __name__ == "__main__":
    unittest.main()
