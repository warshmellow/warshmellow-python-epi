import unittest

import arraysepi
from ddt import data, ddt, unpack


@ddt
class TestArraysEpi(unittest.TestCase):
    def test_sumsum(self):
        nums = [1, 2, 3]
        self.assertEqual(arraysepi.mysum(nums), sum(nums))

    @data((3, [0, 1, 2, 0, 2, 1, 1], [0, 0, 1, 2, 2, 1, 1]))
    @unpack
    def test_dutch(self, idx, nums, expected):
        result = arraysepi.dutch(idx, nums)
        self.assertEqual(result, expected)
