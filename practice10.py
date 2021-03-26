# coding=UTF-8
"""
@Time：2021/3/25 15:40
@Author：Administrator
@Project:pythonProject1
@Name:practice10 
"""
# static定义静态变量的用法
# 使用auto 定义变量用法

from Tkinter import *

canvas = Canvas(width=800, height=600, bg='yellow')
canvas.pack(expand=YES, fill=BOTH)
k = 1
j = 1
for i in range(0, 26):
    canvas.create_oval(310 - k, 250 - k, 310 + k, 250 + k, width=1)
    k += j
    j += 0.3
    mainloop()
