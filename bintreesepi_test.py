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

    # 9.12
    def test_reconstruct(self):
        a = BinTree(item='a')
        f = BinTree(item='f')
        e = BinTree(item='e', left=a)
        b = BinTree(item='b', left=f, right=e)

        i = BinTree(item='i')
        g = BinTree(item='g', left=i)
        d = BinTree(item='d', right=g)
        c = BinTree(item='c', right=d)

        h = BinTree(item='h', left=b, right=c)

        reconstructed = BinTree.reconstruct(inorder="fbaehcdig",
                                            preorder="hbfeacdgi")

        self.assertEqual(BinTree.inorder(reconstructed), "fbaehcdig")
        self.assertEqual(BinTree.preorder(reconstructed), "hbfaecdgi")


if __name__ == '__main__':
    unittest.main()
