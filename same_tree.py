#
# 54 / 54 test cases passed.
# Status: Accepted
# Runtime: 44 ms

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif not p or not q:
            return False
        
        if p.left and q.left and p.right and q.right:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right) and p.val == q.val
        elif p.left and q.left and not p.right and not q.right:
            return self.isSameTree(p.left, q.left) and p.val == q.val 
        elif not p.left and not q.left and p.right and q.right:
            return self.isSameTree(p.right, q.right) and p.val == q.val
        elif not (p.left or p.right or q.left or q.right):
            return p.val == q.val
        else:
            return False
