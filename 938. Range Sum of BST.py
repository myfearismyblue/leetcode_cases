# Given the root node of a binary search tree and two integers low and high,
# return the sum of values of all nodes with a value in the inclusive range [low, high].
#
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        recur_this = root.val if low <= root.val <= high else 0
        recur_left, recur_right = 0, 0
        if root.val != None
            recur_left = self.rangeSumBST(root.left, low, high) if low <= self.rangeSumBST(root.left, low,
                                                                                                 high) <= high else 0
            recur_right = self.rangeSumBST(root.right, low, high) if low <= self.rangeSumBST(root.right, low,
                                                                                                high) <= high else 0
        answer = recur_this + recur_left + recur_right

        return answer



