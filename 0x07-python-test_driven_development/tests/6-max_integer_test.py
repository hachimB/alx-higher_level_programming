#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestMaxInteger class"""
    def test_1(self):
        self.assertEqual(max_integer([1, 3, 16]), 16)

    def test_2(self):
        self.assertEqual(max_integer([1, 80, 16, 56]), 80)

    def test_3(self):
        self.assertEqual(max_integer([499, 30, 16, 90]), 499)

    def test_4(self):
        self.assertEqual(max_integer([]), None)

    def test_5(self):
        self.assertEqual(max_integer([15]), 15)

    def test_6(self):
        self.assertEqual(max_integer([1.3, 3.5, 16.5]), 16.5)

    def test_7(self):
        self.assertEqual(max_integer([-1, -3, -16]), -1)

    def test_8(self):
        self.assertEqual(max_integer([-1, 3.5, -16]), 3.5)

    def test_9(self):
        self.assertEqual(max_integer(["Ali", "Issa", "Salman"]), "Salman")

    def test_10(self):
        self.assertEqual(max_integer("str"), "t")

    def test_11(self):
        self.assertEqual(max_integer(""), None)

    def test_12(self):
        self.assertEqual(max_integer([None]), None)
