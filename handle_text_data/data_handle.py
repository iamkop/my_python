# -*- coding:utf-8 -*-

"""
假设处理四个选手的跑步数据,数据文件为play_1-4.txt
"""

try:
    with open("play_1.txt", encoding="utf-8") as p_1:
        data = p_1.readline()
    play_1 = data.strip().split(",")
    print("【play_1数据】", play_1)

    with open("play_2.txt", encoding="utf-8") as p_2:
        data = p_2.readline()
    play_2 = data.strip().split(",")
    print("【play_2数据】", play_2)

    with open("play_3.txt", encoding="utf-8") as p_3:
        data = p_3.readline()
    play_3 = data.strip().split(",")
    print("【play_3数据】", play_3)

    with open("play_4.txt", encoding="utf-8") as p_4:
        data = p_4.readline()
    play_4 = data.strip().split(",")
    print("【play_4数据】", play_4)

except IOError as error:
    print("异常错误!", error)

# 如果对四组数据进行排序,两种办法,复制排序和原地排序
# 原地排序
test_1 = [9, 6, 8, 7, 2, 1, 3, 5, 4]
test_1.sort()
print("【原地排序】", test_1)
# 复制排序
test_2 = [9, 6, 8, 7, 2, 1, 3, 5, 4]
print("【复制排序】", sorted(test_2))
print("【复制排序】", "原来的test_2的值还在: ", test_2)

"""但是对于实验数据来说,时间有的是 2:39,还有个别是2-39
那么就应该先让数据格式一致,再做排序!定义一个方法:trans()
"""


def trans(time_string):
    if ":" in time_string:
        splitter = ":"
    elif "-" in time_string:
        splitter = "-"
    else:
        return time_string
    (mint, sec) = time_string.split(splitter)
    return mint + "." + sec


play_1_format = []
play_2_format = []
play_3_format = []
play_4_format = []

for ts in play_1:
    p1 = trans(ts)
    play_1_format.append(p1)
for ts in play_2:
    p2 = trans(ts)
    play_2_format.append(p2)
for ts in play_3:
    p3 = trans(ts)
    play_3_format.append(p3)
for ts in play_4:
    p4 = trans(ts)
    play_4_format.append(p4)
print("【格式化后play_1】", play_1_format)
print("【格式化后play_2】", play_2_format)
print("【格式化后play_3】", play_3_format)
print("【格式化后play_4】", play_4_format)
print("【排序后play_1】", sorted(play_1_format))
print("【排序后play_2】", sorted(play_2_format))
print("【排序后play_3】", sorted(play_3_format))
print("【排序后play_4】", sorted(play_4_format))
# 关于列表推到上面的在做转换的时候,是比较麻烦的!
# 可以改写成一下的方案!(推导列表)
# trans:转换的函数,each_str:列表里每个元素,play_1:需要遍历的列表
play_1_format = [trans(each_str) for each_str in play_1]
print("【推导列表示例】",play_1_format)