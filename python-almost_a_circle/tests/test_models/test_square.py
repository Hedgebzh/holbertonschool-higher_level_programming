#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from models.square import Square

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
      s.update(89, 2)
      self.assertEqual("[Square] (89) 5/5 - 2", str(s))

    def test_update_three_args(self):
      """Test update function with three args"""
      s = Square(5, 5, 5, 5)
      s.update(89, 2, 3)
      self.assertEqual("[Square] (89) 5/5 - 2", str(s))

    def test_update_four_args(self):
      """Test update function with four args"""
      s = Square(5, 5, 5, 5)
      s.update(89, 2, 3, 4)
      self.assertEqual("[Square] (89) 4/5 - 2", str(s))




if __name__ == "__main__":
    unittest.main()
