import unittest

import hypothesis.strategies as st
from hypothesis import given

from arraysepi import *


class TestArraysEpi(unittest.TestCase):

    @given(st.lists(
        elements=st.integers(),
        min_size=1,
        unique=True
    ))
    def test_dutch(self, nums: List[int]):
        idx = len(nums) // 2
        dist = nums[idx]

        result = dutch(idx, nums)
        new_idx = result.index(dist)

        all_lt = True
        for _, num in enumerate(nums[:new_idx]):
            if num >= dist:
                all_lt = False
                break

        all_gt = True
        for _, num in enumerate(nums[new_idx + 1:]):
            if num <= dist:
                all_gt = False
                break

        self.assertTrue(all_lt and all_gt)

    @given(st.lists(
        elements=st.integers(),
        min_size=1
    ))
    def test_mod_three_sort(self, nums: List[int]):
        result = mod_three_sort(nums)

        increasing = True
        for i in range(1, len(result)):
            n, m = result[i - 1], result[i]
            if (n % 3) > (m % 3):
                increasing = False

        self.assertTrue(increasing)

    @given(st.lists(
        elements=st.integers(),
        min_size=1
    ))
    def test_mod_two_stable_sort(self, nums: List[int]):
        odds = [x for x in nums if x % 2 != 0]

        result = mod_two_stable_sort(nums)

        increasing = True
        for i in range(1, len(result)):
            n, m = result[i - 1], result[i]
            if (n % 2) > (m % 2):
                increasing = False

        self.assertTrue(increasing)

        sorted_odds = [x for x in result if x % 2 != 0]

        self.assertListEqual(odds, sorted_odds)
