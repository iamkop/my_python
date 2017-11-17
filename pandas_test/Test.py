# -*- coding: UTF-8 -*-
import pandas as pd
from pandas import Series,DataFrame


def read_excel():
    df = pd.read_excel("C:\\Users\\DELL\\Desktop\\feng.xlsx", heard=0)
    head = df.head(3)
    columns = df.columns = ["1", "2", "3", "4"]
    print(len(df))


read_excel();
