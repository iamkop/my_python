# -*- coding:utf-8 -*-

"""简单函数说明
"""


def fun1(username, password="myPassword"):
    """最简单的函数,可以指定参数默认值,不传入参数则用默认值
    """
    print("【基本函数】", "我的名字是: {},密码默认是: {}".format(username, password))


def fun2():
    """可以将函数赋值给变量
    """
    # 将函数赋值给变量'f',没有使用(),因为并不是在调用fun1函数
    # 只是将fun1()放在变量f里
    f = fun1
    print("【函数赋值给变量】", "变量f的类型是", type(f))
    # 如果要执行f
    f("jim")


def fun3():
    """函数中,也可以定义函数,不过在fun3()以外,是无法调用起内部函数的
    """
    print("【内部函数】", "这里是fun3()")

    def fun3_1():
        print("【内部函数】", "这里是fun3_1()")

    def fun3_2():
        print("【内部函数】", "这里是fun3_2()")

    # 不用下面两行代码,两个内部函数不会执行
    fun3_1()
    fun3_2()


def fun4(which):
    """函数,返回函数,就是说,某函数的返回值不是具体值,而是函数
    """

    def fun4_1():
        print("【返回函数】", "这里是fun4_1()")

    def fun4_2():
        print("【返回函数】", "这里是fun4_2()")

    if which == "fun4_1":
        # 注意,这里是fun4_1,不是fun4_1()
        # 如果加了(),就不会成功返回函数,因为,函数已经执行完
        # 这里返回函数,是返回函数定义而已
        return fun4_1
    else:
        return fun4_2


def fun5_1():
    """将函数传给函数_1,一个场景,比如在之前fun1之前,先做点别的事儿
    """
    print("【函数接受函数参数】", "我去做火车!")


def fun5_2(fun):
    """将函数传给函数_2
    """
    print("【函数接受函数参数】", "我去买火车票!")
    fun()


# fun1("jack")
# fun2()
# fun3()
# 执行fun4()

# fun_ = fun4("fun4_1")
# print(fun_)
# fun_()

# fun5_2(fun5_1)
