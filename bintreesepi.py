class BinTree:
    def __init__(self, item=None, left=None, right=None, parent=None):
        self.item = item
        self.parent = parent
        self.left = left
        self.right = right

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
