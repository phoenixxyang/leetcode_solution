# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0;
        
        left_depth = self.maxDepth(root.left) 
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1




if __name__ == '__main__':
    root = node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.right = node6
    node5.left = node7

    print Solution().maxDepth(root)
