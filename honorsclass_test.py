import unittest

import hypothesis.strategies as st
from hypothesis import given

from honorsclass import *


class TestHonorsClass(unittest.TestCase):
    @given(st.integers(min_value=1), st.integers(min_value=1))
    def test_bin_gcd(self, a, b):
        result = bin_gcd(a, b)
        self.assertEqual(a % result, 0)
        self.assertEqual(b % result, 0)
        self.assertEqual(result, bin_gcd(a, b % a))
