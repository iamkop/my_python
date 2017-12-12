# -*- coding: utf-8 -*-
#coding=utf-8

import urllib.request as req
import datetime
from lxml import etree
import pymysql

# 博客地址，{page_num}是要传入的页码数量
base_url = "http://blog.csdn.net/i_am_kop/article/list/{page_num}"


def get_html(url):
    # 当前页数
    page_num = 1
    # 利用mysql批量插入，这里是values后面的值
    sql_fra = []
    while True:
        print(100 * "-")
        print("第", page_num, "页")
        print(100 * "-")
        # 获取页面
        page = req.urlopen(url.format(page_num=page_num))
        html = page.read().decode("utf-8")
        # 开始解析xpath
        selector = etree.HTML(html)
        # 博客列表的div
        blog_divs = selector.xpath("//*[@id=\"article_list\"]/div[*]")
        # 如果此页没有内容，说明所有博客已经爬取完毕，退出
        if not blog_divs:
            break
        # 循环读取本业博客
        for blog_div in blog_divs:
            # 标题
            title_ele = blog_div.xpath("div[1]/h1/span/a")[0]
            title = title_ele.xpath("string(.)").replace(" ", "").replace("\r\n", "")
            # 数量
            count_ele = blog_div.xpath("div[3]/span[2]")[0]
            count = count_ele.xpath("string(.)").replace("阅读(", "").replace(")", "")
            # 当前时间
            now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # print("({title},{count},{date})".format(title=title, count=count, date=now))
            sql_fra.append("('{title}',{count},'{date}')".format(title=title, count=count, date=now))
        page_num += 1
    # print(sql_fra)
    # 开始插入mysql
    conn = pymysql.connect(host='XXXX', port=3306, user='root', passwd='Password', db='blog_log')
    cursor = conn.cursor()
    sql = "INSERT INTO t_read_num(title,read_count,create_date) VALUES "+",".join(sql_fra)
    conn.set_charset("utf8")
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

get_html(base_url)