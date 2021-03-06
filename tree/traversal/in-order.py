# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        if not root:
            return ret

        def helper(root):
            if root is not None:
                helper(root.left)
                ret.append(root.val)
                helper(root.right)
            else:
                return

        helper(root)
        return ret