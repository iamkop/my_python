# -*- coding: UTF-8 -*-

"""
四个数字分别是：1、2、3、4
提问：能组成多少个互不相同且无重复数字的三位数？各是多少？
"""

def method_1():
    for num_0 in range(1, 5):
        for num_1 in range(1, 5):
            for num_2 in range(1, 5):
                if (num_0 != num_1) and (num_0 != num_2) and (num_2 != num_1):
                    print(num_0, num_1, num_2)

method_1()
