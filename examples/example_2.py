# -*- coding: UTF-8 -*-
import math

"""
一个整数，它加上100和加上268后都是一个完全平方数
提问：请问该数是多少？
"""

begin = 1


def method_1():
    for i in range(1, 10000):
        x = math.sqrt(i + 100)
        y = math.sqrt(i + 268)
        print(x)
        print(y)
        if type(x) == int and type(y) == int:
            print(i)


method_1()
