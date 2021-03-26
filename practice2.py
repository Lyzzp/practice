# coding=UTF-8
"""
@Time：2021/3/19 8:39
@Author：Administrator
@Project:pythonProject1
@Name:practice2 
"""
# 对十个数进行排序，利用选择法，从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换
N = 10
# print '请输入10个数：\n'
k = []
for i in range(N):
    k.append(int(raw_input('input a number:')))
print k
for i in range(N):
    print k[i]
for i in range(N - 1):
    min = i
    for j in range(i + 1, N):
        if k[min] > k[j]:
            min = j
            k[i], k[min] = k[min], k[i]
print 'after sort'
for i in range(N):
    print k[i]
