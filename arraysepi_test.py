import unittest

import arraysepi


class TestArraysEpi(unittest.TestCase):
    def test_dutch(self):
        idx = 3
        nums = [0, 1, 2, 0, 2, 1, 1]
        expected = [0, 0, 1, 2, 2, 1, 1]
        result = arraysepi.dutch(idx, nums)
        self.assertEqual(result, expected)
