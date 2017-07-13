# -*- coding:utf-8 -*-

def read_file():
    """
    读取数据,这里只是简单的数据文件读取
    """
    # 读取目标路径的文件
    data = open("C:\\Users\\DELL\Desktop\\test_data", encoding="utf-8")
    # 打印第一行和第二行!
    print("【数据读取】", "第一行数据: ", data.readline())
    print("【数据读取】", "第二行数据: ", data.readline())
    # 读取所有数据,如果顺着代码执行下来,下面循环会是从第三行开始打印
    # 为了让这个循环回到第一行开始,使用seek()函数
    data.seek(0)
    i = 1
    for every_line in data:
        print("【数据读取】", "读取所有行数据,第", i, "行: ", every_line)
        i += 1
    # 关闭data对象
    data.close()
    # 是否已经关闭
    print(data.closed)


def format_data():
    """固定格式的数据处理,数据示例:
    name:jim
    age:29
    sex:man
    home:beijing
    """
    data = open("C:\\Users\\DELL\Desktop\\test_data", encoding="utf-8")
    for every_line in data:
        # 以:分割数据,得到的是一个set
        split = every_line.split(":")
        # 将set的两个值,分别处理给两个变量
        (key, value) = split
        print("【数据分割】", "key: ", key, " value", value)
        # 如果改变数据,例如: age:29 --> age:29:hello
        # 那么会抛出异常,因为分割出三部分,但是赋值被两个变量,可以考虑这么解决
        # every_line.split(":") --> every_line.split(":", 1)
        # 就是说,参数maxsplit=1,那么会分割一次,后面的会忽略!


def format_data_exception():
    """format_data()方法中,多:的情况下会抛出异常,
    为了解决异常,在split()方法中增加了参数:1
    但是有更多的非正常情况的话,可以引入异常机制,形式和java基本一样,示例数据:
    name:jim
    age:29
    sex:man
    home:beijing:exception
    """
    data = open("C:\\Users\\DELL\Desktop\\test_data", encoding="utf-8")
    for every_line in data:
        try:
            split = every_line.split(":")
            (key, value) = split
            print("【异常处理】", "key: ", key, " value", value)
            data.close()
        except:
            print("【异常处理】", "数据读取发生错误改行数据为: ", every_line)
        finally:
            # 当异常发生时,data.close()不会执行,类似java,引入finally
            # 首先判断data对象存在,和没有关闭
            if "data" in locals() and not data.closed:
                data.close()


def write_data():
    """将下列数据,写入到out.txt
    name:jim
    age:29
    sex:man
    home:beijing
    """
    data = open("C:\\Users\\DELL\Desktop\\test_data", encoding="utf-8")
    # 创建一个输出out对象,param1:写出的文件名,param2:写模式(write)
    out = open("out.txt", "w")
    for every_line in data:
        # 逐行写入
        print(every_line, file=out)
    # 关闭输出流
    out.close()


def with_as():
    """使用with,可以代替format_data_exception()方法的try/except/finally
    在with语法上,因为data.close()操作,python解释器会自动进行close操作
    with语法有些类似oracle的 with....as...
    这是利用了"上下文管理协议"的技术!
    """
    try:
        data = open("C:\\Users\\DELL\Desktop\\test_data_1", encoding="utf-8")
        print(data.readline())
    except IOError:
        print("【异常处理】", "发生异常!文件不存在")
    finally:
        if "data" in locals() and not data.closed:
            data.close()
    # 上面的代码可以改成下面
    try:
        with open("C:\\Users\\DELL\Desktop\\test_data_1", encoding="utf-8") as data:
            print(data.readline())
    except IOError as error:
        print("【异常处理】", "发生异常!文件不存在")


# read_file()
# format_data()
# format_data_exception()
# write_data()
with_as()
