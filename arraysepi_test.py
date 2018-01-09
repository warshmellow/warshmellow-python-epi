import unittest
from typing import List

import hypothesis.strategies as st
from hypothesis import given

import arraysepi


class TestArraysEpi(unittest.TestCase):

    @given(st.lists(
        elements=st.integers(),
        min_size=1,
        unique=True
    ))
    def test_dutch(self, nums: List[int]):
        idx = len(nums) // 2
        dist = nums[idx]

        result = arraysepi.dutch(idx, nums)
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
