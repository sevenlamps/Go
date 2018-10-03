from constants import *


class TreeNode(object):
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.child_left: TreeNode = left
        self.child_right: TreeNode = right
        self.parent: TreeNode = parent

    def has_left_child(self) -> bool:
        return self.child_left is not None

    def has_right_child(self) -> bool:
        return self.child_right is not None

    def is_left_child(self) -> bool:
        return self.parent and self.parent.child_left == self

    def is_right_child(self) -> bool:
        return self.parent and self.parent.child_right == self

    def is_root(self) -> bool:
        return not self.parent

    def if_leaf(self):
        return not (self.child_left or self.child_right)

    def has_any_children(self):
        return self.child_left or self.child_left

    def has_both_children(self):
        return self.child_left and self.child_right

    def replace_node_data(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.child_left = lc
        self.child_right = rc
        if self.has_left_child():
            self.child_left.parent = self
        if self.has_right_child():
            self.child_right.parent = self


class BinarySearchTree(object):
    root: TreeNode = None
    size: int = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    # def __iter__(self):
    #     return self.root.__iter__()
    #



