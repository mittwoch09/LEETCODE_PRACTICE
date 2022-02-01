# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = [root, root]
        while stack:
            n1 = stack.pop()
            n2 = stack.pop()
            if (n1 and n2) is None:
                if n1 is n2:
                    continue
                return False
            if n1.val != n2.val:
                return False
            stack.extend([n1.left, n2.right, n1.right, n2.left])
        return True