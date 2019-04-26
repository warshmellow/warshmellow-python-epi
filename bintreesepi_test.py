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

        expected_inorder, expected_preorder = "fbaehcdig", "hbfeacdgi"

        reconstructed = BinTree.reconstruct(inorder=expected_inorder,
                                            preorder=expected_preorder)

        self.assertEqual("".join(BinTree.inorder(reconstructed)),
                         expected_inorder)
        self.assertEqual("".join(BinTree.preorder(reconstructed)),
                         expected_preorder)

    # 9.13
    def test_reconstruct_with_marker(self):
        """
        h
            c
                d
                    g
                        -
                        i
            b
                e
                    -
                    a
                f
        """

        expected_inorder, expected_preorder = "fbaehcdig", "hbfeacdgi"
        preorder_blueprint = [
            'h', 'b', 'f', '', '', 'e', 'a', '', '', '', 'c', '', 'd', '', 'g',
            'i', '', '', ''
        ]

        reconstructed = BinTree.reconstruct_with_marker(preorder_blueprint)

        self.assertEqual("".join(BinTree.inorder(reconstructed)),
                         expected_inorder)
        self.assertEqual("".join(BinTree.preorder(reconstructed)),
                         expected_preorder)

    # 9.13 Variant
    @unittest.skip("weird flipping")
    def test_reconstruct_from_postorder(self):
        """
        h
            c
                d
                    g
                        -
                        i
        """

        expected_inorder, expected_preorder, expected_postorder = "igdch", "hcdgi", "igdch"
        postorder_blueprint = ['', '', 'i', '', 'g', '', 'd', '', 'c', '', 'h']

        reconstructed = BinTree.reconstruct_from_postorder(postorder_blueprint)

        self.assertEqual("".join(BinTree.inorder(reconstructed)),
                         expected_inorder)
        self.assertEqual("".join(BinTree.preorder(reconstructed)),
                         expected_preorder)
        self.assertEqual("".join(BinTree.postorder(reconstructed)),
                         expected_postorder)


if __name__ == '__main__':
    unittest.main()
