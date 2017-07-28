# -*- coding:utf-8 -*-

"""
字符串的一些处理
"""

username = "jack"
password = "yourPassword"
out = "我的用户名是:{0},密码是{1}".format(username, password)
print("【字符拼接】", out)

str_list = ["jack", "GOOGLE", "java", 1]
str_1 = "aaa\nbbb\nccc"
print("【以回车分割字符并转为数组】", str_1.splitlines())
print("【计算字符串中字符数量】", "'password'中有{0}个's'".format(password.count("s")))
print("【大小写】", "ABCde 转换为大小写", "ABCde".lower(), "ABCde".upper())

# 处理url参数
url = "user=pilgrim&database=master&password=PapayaWhip"
split = url.split("&")
print("【URL处理-1】", "以'&'进行切割", split)
final = [v.split("=") for v in split]
print("【URL处理-2】", "再次切割处理", final)
print("【URL处理-3】", "最终得到参数字典", dict(final))

# 字符的分片(slice),和集合的分片差不多
str_slice = "what are you doing?"
print("【分片】", "0位置开始取,取到4的前一位置", str_slice[0:4])
print("【分片】", "0位置开始取,取到倒数第二个字符", str_slice[0:-1])
print("【分片】", "0位置开始取,取到后面所有字符", str_slice[0:])
print("【分片】", "取1以前所有字符(不包括1)", str_slice[:1])

# bytes 字节类型
# 前方加一个'b'即声明字节类型
byte_1 = b"\x65"
print("【字节类型】","b'\\x65'的类型是{}".format(type(byte_1)))
