# coding=UTF-8
"""
@Time：2021/3/18 9:41
@Author：Administrator
@Project:pythonProject1
@Name:practice1 
"""

# 「快乐数」定义为：
#
# 对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
# 然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
# 如果 可以变为1，那么这个数就是快乐数。
# 如果 n 是快乐数就返回 true ；不是，则返回 false 。
#
from math import sqrt


class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        list1 = []
        flag = 1
        while flag:
            for i in range(str(n)):
                list1.append(int(i))
                if sum(sqrt(list1[int(i)])) == 1:
                    flag == 0
                    return True
                else:
                    print "这个数一点都不快乐"
                    return False

        print "我也想像它一样快乐"


s = Solution()
s.isHappy(19)
