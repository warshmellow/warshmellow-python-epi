class BinTree:
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right

    @staticmethod
    def inorder(root):
        if not root:
            return []

        result = []
        result.extend(BinTree.inorder(root.left))
        result.extend([root.item])
        result.extend(BinTree.inorder(root.right))
        return result

    @staticmethod
    def preorder(root):
        if not root:
            return []

        result = []
        result.extend([root.item])
        result.extend(BinTree.preorder(root.left))
        result.extend(BinTree.preorder(root.right))
        return result

    @staticmethod
    def height(root):
        if not root:
            return -1

        return max(BinTree.height(root.left), BinTree.height(root.right)) + 1

    @staticmethod
    def is_height_balanced(root):
        """
        A
            B
            C
                D
                E
                    F
        """
        # none case
        if not root:
            return True

        # recursive case
        return BinTree.is_height_balanced(
            root.left) and BinTree.is_height_balanced(root.right) and abs(
                BinTree.height(root.left) - BinTree.height(root.right)) <= 1

    @classmethod
    def reconstruct(cls, inorder, preorder):
        if len(inorder) == 0 or len(preorder) == 0:
            return

        root_item = preorder[0]

        root_idx_in_inorder = inorder.index(root_item)
        left_inorder = inorder[:root_idx_in_inorder]
        right_inorder = inorder[root_idx_in_inorder + 1:]

        left_preorder = preorder[1:root_idx_in_inorder + 1]
        right_preorder = preorder[root_idx_in_inorder + 1:]

        left_subtree = cls.reconstruct(left_inorder, left_preorder)
        right_subtree = cls.reconstruct(right_inorder, right_preorder)

        return cls(item=root_item, left=left_subtree, right=right_subtree)

    @classmethod
    def reconstruct_with_marker(cls, preorder_with_marker):
        return cls(item=preorder_with_marker[0])
