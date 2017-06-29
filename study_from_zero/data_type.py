# python的数据类型

import fractions


def python_boolean():
    """
    布尔类型,这块内容较少
    """
    boolean1 = True
    boolean2 = False
    if boolean1:
        print("【if应用】", "true")
    else:
        print("【if应用】", "false")
    #: 布尔值是可以做数学运算的,true 1,false 0
    print("【数学运算】", "布尔值是可以做数学运算的(p2的遗留问题,不建议这么做),那么true+true = " + str(boolean1 + boolean2))
    # 整数0值代表false,非0值代表true
    # 空列表为false,非空列表为true
    if "33":
        print("【0与非0值】", "123是非0值,代表 true")
    if 0:
        print("【0与非0值】", "0代表false,所以此处不会被打印!")


def python_number():
    """
    Python 同时支持Integer［整型］和Floating Point［浮点型］数值。无任何类型
    声明可用于区分；Python 通过是否有小数点来分辨它们。
    浮点型精确到小数点后15位,int则无限大
    """
    print("【数据类型】", "1 的数据类型是: " + str(type(1)))
    print("【数据类型】", "1.0 的数据类型是: " + str(type(1.0)))
    print("【数据类型】", "判断param1是否是param2的类型: " + str(isinstance(1, int)))
    # 数值之间的强制转换
    print("【转换】", "2 --> float:", float(2))
    # 只是取整并非四舍五入
    print("【取整】", "2.0 --> float:", int(2.0))
    print("【取整】", "2.8 --> float:", int(2.8))
    print("【取整】", "-2.8 --> int:", int(-2.8))
    #: 分数计算
    x = fractions.Fraction(1, 3)
    print("【分数】", "分数 X 的值是:", x, "那么 2*x 的值是:", 2 * x)
    y = fractions.Fraction(4, 6)
    print("【分数】", "分数 Y 的值是:", y)
    #: z = fractions.Fraction(4, 0)
    #: print("【分数】", "分母为0,报错!", z)


def python_list():
    """列表的python重要数据集合类型,长度可变
    可以容纳不同对象
    """
    # 如何创建列表?
    list_1 = ["a", "b", 1, "c"]
    print("【创建,索引】", "列表list_1的值为:", list_1, "第一个值为:", list_1[0])
    # 负数索引
    print("【创建,索引】", "列表list_1的-1处值为:", list_1[-1], "列表list_1的-2处值为:", list_1[-2])
    #: 列表切片
    #: 可从其中获取任何部分作为新列表,称为对列表进行切片
    #: 可以根据下面实例理解
    print("【切片】", "从index1开始取,取到index3,但是不包括index3:", list_1[1:3])
    print("【切片】", "从index1开始取,取到index-1:", list_1[1:-1])
    print("【切片】", "省略冒号前面的值,即表示从0开始:", list_1[:3])
    print("【切片】", "省略冒号后面的值,即表示从1开始取全部:", list_1[1:])
    print("【切片】", "省略冒号前后的值,表示取全部:", list_1[:])
    # 向列表中新增项,共4种方法
    print("【增加元素】", "method1: 两列表相加", list_1 + [2.4, "d"])
    #: method需要注意,这里不要试图list_1 = list_1.append("3")再打印list1
    #: 或者直接打印list_1.append("3"),因为此方法返回值为none,要么打印的none,
    #: 要么将none赋值给list_1,所以上述两种情况打印的都是none
    list_1.append(True)
    print("【增加元素】", "method2: 向末尾增加元素", list_1)
    list_1.extend(["d", "e"])
    print("【增加元素】", "method3: 增加一个列表的所有元素到末尾", list_1)
    list_1.insert(0, "A")
    print("【增加元素】", "method4: 指定角标进行插入,原有角标依次向后迁移", list_1)
    # 列表对值的检索
    list_2 = ["a", "b", "c", "a", "c"]
    print("【检索】", "list_2中 a 的数量: ", list_2.count("c"))
    print("【检索】", "list_2中是否包含a: ", "a" in list_2)
    print("【检索】", "list_2中 a 的角标(多值则只计算第一个,不包含则异常): ", list_2.index("a"))
    # 删除元素
    list_3 = ["a", "b", "c", "d", "e"]
    del list_3[0]
    print("【删除元素】", "通过索引删除: ", list_3)
    list_3.remove("e")
    print("【删除元素】", "通过值删除: ", list_3)
    # pop()函数,如果不传参数,则删除最后一元素,传值,则删除指定角标,返回值是被删除的元素
    list_4 = ["a", "b", "c", "d", "e"]
    print("【删除元素】", "通过pop删除: ", list_4.pop())
    print("【删除元素】", "通过pop删除: ", list_4.pop(0))
    print("【删除元素】", "list_4最后的值为: ", list_4)


def python_tuple():
    """元组,不可变的列表。一旦创建之后，用任何方法都不可以修改元素
    """
    # 元组定义,索引下标等和list基本相同
    # 除了list增删改的方法外,包括切片等方法元组都支持
    tuple_1 = ("a", "b", "c", 1)
    print("【创建】", "tuple_1的值为: ", tuple_1)
    # 利用元组赋多值
    # 在 Python 中，可使用元组来一次赋多值
    tuple_2 = ("a", 5, True)
    (x, y, z) = tuple_2
    print("【赋多值】", "x=", x, "y=", y, "z=", z)


def python_set():
    """集合 set 是装有独特值的无序“袋子”。一个简单的集合可以包含
        任何数据类型的值。如果有两个集合，则可以执行像联合、交
        集以及集合求差等标准集合运算。注意,区别于列表,集合时无序的,这个有些像java
        另外,集合不允许有重复值
    """
    # 创建集合
    set_1 = {1, 2}
    list_1 = ["a", "b", 3.14]
    print("【创建】", "set_1的值为: ", set_1)
    print("【创建】", "以列表为基础创建集合: ", set(list_1))
    # 增加值
    set_2 = {1, 2, 3}
    set_2.add(4)
    print("【增加】", "set_2的值为: ", set_2)
    # 修改 故名思议,save or update !
    set_3 = {1, 2, 3}
    set_3.update({3, 4, 5})
    print("【修改】", "set_3的值为: ", set_3)
    set_4 = {1, 2, 3}
    set_4.update({2, 3, 4}, {4, 5, 6})
    print("【修改】", "可以加两个或以上的参数,set_4的值为: ", set_4)
    # 删除值
    # 两种删除的方法,区别就是,删除一个不存在值的时候
    # remove抛异常,discard不抛出异常
    # set也有pop删除方法
    set_5 = {1, 2, 3, 4, 5, 6}
    set_5.remove(1)
    print("【删除】", "method1: 利用remove()删除", set_5)
    set_5.discard(4)
    print("【删除】", "method2: 利用discard()删除", set_5)
    # 运算
    set_6 = {1, 2, 3, 4, 5, 6}
    set_7 = {3, 4, 5, 6, 7, 8}
    print("【运算】", "3是否存在于 set_6 内: ", 3 in set_6)
    print("【运算】", "合并 set_6 和 set_7: ", set_6.union(set_7))
    print("【运算】", "set_6 和 set_7 的交集: ", set_6.intersection(set_7))
    print("【运算】", "set_6 出现的,但未在 set_7 的元素: ", set_6.difference(set_7))
    print("【运算】", "没有同时出现在 set_6 和 set_7 的元素: ", set_6.symmetric_difference(set_7))


def python_dict():
    """字典相当于java中的map
    """
    # 创建
    dict_1 = {"key1": "value1"}
    print("【删除】", "创建字典 dict_1: ", dict_1)
    # 修改
    dict_1["key1"] = "new value"
    print("【修改】", "修改字典 dict_1: ", dict_1)


# python_number()
# python_boolean()
# python_list()
# python_tuple()
# python_set()
python_dict()
