# coding=UTF-8
"""
@Time：2021/3/26 9:22
@Author：Administrator
@Project:pythonProject1
@Name:practice11
判断对称二叉树
"""


class Solution(object):
    def isSymmetric(self, root):
        if not root:
            return True

        def dfs(left, right):
            if not (left or right):
                return True
            if not (left and right):
                return False
            if left.val != right.val:
                return False
            return dfs(left.left, right.right) and dfs(left.right, right.left)

        return dfs(root.left, root.right)
