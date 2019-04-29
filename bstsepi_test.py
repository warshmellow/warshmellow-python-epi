import unittest

import hypothesis.strategies as st
from hypothesis import given

from hashtablesepi import *

from bintreesepi import BinTree


class TestBinTreesEpi(unittest.TestCase):

    @unittest.skip("weird flipping")
    def test_is_bst(self):
        """
        7
            11
                17
                    -
                    13
            3
                5
                2
        """
        """
        43
            47
                53
            23
                37
                    41
                    29
                        31
        """
        pass


if __name__ == '__main__':
    unittest.main()
