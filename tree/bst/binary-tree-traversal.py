# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = [[]for _ in range(self.getHeight(root))]
        self.traversal(root, 0, ret)
        return ret

    def getHeight(self, root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1

    def traversal(self, root, level, ret):
        if root is None:
            return
        ret[level].append(root.val)
        self.traversal(root.left, level+1, ret)
        self.traversal(root.right, level+1, ret)


