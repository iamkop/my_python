# -*- coding: utf-8 -*-
# coding=utf-8

import pandas as pd
import pymysql
from pandas import DataFrame as df

conn = pymysql.connect(host='101.200.83.54', port=3306, user='root', passwd='Password!1', db='blog_log')
conn.set_charset("utf8")
sql_result = pd.read_sql('select * from t_read_num t ', con=conn)
print(sql_result)