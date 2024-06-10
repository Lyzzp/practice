# coding=UTF-8
"""
@Time：2021/3/26 15:13
@Author：Administrator
@Project:pythonProject1
@Name:practice13 
"""


class ListNode(object):
    def __init__(self, data, p=None):
        self.data = data
        self.next = p


class Linklist(object):
    def __init__(self):
        self.head = None

    def set(self):  # 初始建立
        print ('input:')
        data = input()
        if data != "":
            self.head = Linklist(int(data))
            p = self.head
        else:
            print ("over!")
            return
        while 1:
            data = input()
            if data != "":
                p.next = ListNode(int(data))
                p = p.next
            else:
                print ("over!")
                break

    @property
    def show(self):  # 遍历链表
        print ("链表如下：")
        p = self.head
        if p == None:
            print ("Empty!")
            return
        while p:
            print (p.data)
            p = p.next
        print ("over!")
        return

    @property
    def isempty(self):  # 判断是否为空
        p = self.head
        if p == None:
            return True
        else:
            return False

    @property
    def length(self):  # 获取长度
        p = self.head
        l = 0
        while p:
            l += 1
            p = p.next
        return l

    def insert(self, data, pos):  # 数据插入
        if self.isempty and pos != 1:
            raise Exception("wrong position!")
        p = self.head
        if pos == 1:
            self.head = ListNode(data)
            self.head.next = p
        n = 2
        while (n < pos) and (p.next != None):
            p = p.next
            n += 1
        if n == pos:
            tmp = p.next
            p.next = ListNode(data)
            p = p.next
            p.next = tmp
        elif n < pos:
            raise Exception("wrong position!")

    def delete(self, pos):  # 删除操作
        p = self.head
        if pos == 1:
            return self.head.next
        for i in range(pos - 2):
            p = p.next
        p.next = p.next.next
#编写一个检查CAN报文值得方法
