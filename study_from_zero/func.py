# 函数


def outer():
    var = "out_var"

    def inner():
        return var

    return inner()


# print(outer)


def lazy_sum(*args):
    def sums():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sums


f = lazy_sum(1, 3, 5, 7, 9)
# 比较两次f函数的打印,不调用就不会运行
print(f)
print(f())


def count():
    """闭包
    """
    fs = []
    for i in range(1, 4):
        def fi():
            return i * i

        fs.append(fi)
    return fs


# f1, f2, f3 = count()
# print(f1())
# print(f2())
# print(f3())


def count1():
    """防止闭包
    """

    def f_1(j):
        def g():
            return j * j

        return g

    fs = []
    for i in range(1, 4):
        fs.append(f_1(i))  # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f1, f2, f3 = count1()
print(f1())
print(f2())
print(f3())

# 匿名函数 和 java里的lambda表达式一样
f = lambda x: x * x

test = list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(test)
