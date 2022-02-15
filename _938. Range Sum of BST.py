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
        answer = 0
        recur_this, recur_left, recur_right = 0, 0, 0
        if root is not None:
            recur_this = root.val if low <= root.val <= high else 0
            recur_left = self.rangeSumBST(root.left, low, high)
            recur_right = self.rangeSumBST(root.right, low, high)
        answer = recur_this + recur_left + recur_right

        return answer

lrl = TreeNode(6)
lll = TreeNode(1)
rr = TreeNode(18)
rl = TreeNode(13)
lr = TreeNode(7, lrl, None)
ll = TreeNode(3, lll, None)
r = TreeNode(15, rl, rr)
l = TreeNode(5, ll, lr)

root1 = TreeNode(10, l, r)
my_sol = Solution()
print(my_sol.rangeSumBST(root1, 6, 10))
