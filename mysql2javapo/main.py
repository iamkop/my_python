# -*- coding: UTF-8 -*-

from mysql2javapo.java_file import JavaFileWriter
from mysql2javapo.mysql_executor import MysqlExecutor

host = 'address'
port = 3306
user = 'root'
passwd = 'password'
db = 'dbName'
get_columns_sql = 'SHOW FULL COLUMNS FROM test.sssss'
package_name = 'com.gzd.po'
path = 'C:\\Users\\DELL\\Desktop\\Test.java'

def main():
    mysql_executor = MysqlExecutor(host=host, port=port, user=user, passwd=passwd, db=db)
    create_sql = mysql_executor.get_columns(get_columns_sql)
    mysql_executor.close()
    print(create_sql)
    # 角标0:列名,1:数据类型,8:注释
    # 生成的结构[[name1,type1,comment2],[name2 ...]]
    columns = []
    for column in create_sql:
        columns_detail = [column[0], column[1].split('(')[0], column[8]]
        columns.append(columns_detail)
    print(columns)

    writer = JavaFileWriter(path, 'utf-8', package_name, columns)
    writer.build_class()


main()


# conn = pymysql.connect(host='101.200.83.54', port=3306, user='root', passwd='Password!1', db='blog_log')
# cursor = conn.cursor()
# sql = 'SHOW FULL COLUMNS FROM blog_log.t_read_num'
# conn.set_charset("utf8")
# cursor.execute(sql)
# fetchall = cursor.fetchall()
# print(fetchall)
# cursor.close()
# conn.close()
