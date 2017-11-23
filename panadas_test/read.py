import pandas as pd
from pandas import DataFrame as df

def read():
    excel = pd.read_excel('C:\\Users\\DELL\\Desktop\\feng.xlsx')
    print(df.head(excel,2))


read()
