# coding=UTF-8
"""
@Time：2021/3/26 10:21
@Author：Administrator
@Project:pythonProject1
@Name:practice12

给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
"""


class Solution(object):
    def levelOrder(self, root):
        '''
        :type root:TreeNode
        :rtype:List[List[int]]
        '''
        if not root:
            return []
        res = []
        queue = [root]
        while queue:
            size = len(queue)
            tmp = []
            for _ in xrange(size):
                r = queue.pop(0)
                tmp.append(r.val)
                if r.left:
                    queue.append(r.left)
                if r.right:
                    queue.append(r.right)
                res.append(tmp)
            return res
