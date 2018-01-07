import unittest

from ddt import data, ddt, unpack

import arraysepi


@ddt
class TestArraysEpi(unittest.TestCase):
    @data((3, [0, 1, 2, 0, 2, 1, 1], [0, 0, 1, 2, 2, 1, 1]))
    @unpack
    def test_dutch(self, idx, nums, expected):
        result = arraysepi.dutch(idx, nums)
        self.assertEqual(result, expected)
