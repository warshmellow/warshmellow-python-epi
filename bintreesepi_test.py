import unittest

import hypothesis.strategies as st
from hypothesis import given

from hashtablesepi import *

from bintreesepi import BinTree


class TestBinTreesEpi(unittest.TestCase):

    # 9.1
    # Check if a tree is height-balance, i.e., for each node of the tree
    # the height between left and right subtrees is at most 1
    def test_is_height_balanced(self):
        """
        A
            B
            C
                D
                E
                    F
        """
        ftree = BinTree()
        etree = BinTree(left=ftree)
        dtree = BinTree()
        ctree = BinTree(left=etree, right=dtree)
        btree = BinTree()
        atree = BinTree(left=ctree, right=btree)

        self.assertEqual(BinTree.is_height_balanced(atree), False, "atree")
        self.assertEqual(BinTree.is_height_balanced(ctree), True, "ctree")


if __name__ == '__main__':
    unittest.main()
