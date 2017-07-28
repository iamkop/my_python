# -*- coding:utf-8 -*-
import re

"""正则表达式
"""


def demo_1():
    """以街道地址为案例
    """
    # 100 NORTH MAIN ROAD
    # 对此街道名做标准化处理,比如,把'ROAD'简写为'RD.'
    s = '100 NORTH MAIN ROAD'
    replace = s.replace('ROAD', 'RD.')
    print('【replace处理】', '把"ROAD"替换为"RD.": ', replace)
    # 当字符串为100 NORTH BROAD ROAD时,简单的替换,就出问题了
    # 那么采取正则的方式,导入re库 import re
    s_1 = '100 NORTH BROAD ROAD'
    print('【正则处理】', re.sub('ROAD$', "RD.", s_1))

demo_1()
