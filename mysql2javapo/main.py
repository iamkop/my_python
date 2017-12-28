# -*- coding: UTF-8 -*-

from mysql2javapo.mysql_executor import MysqlExecutor

host = 'xxxx'
port = 3306
user = 'root'
passwd = 'xxxx!1'
db = 'blog_log'
column_count_sql = 'desc blog_log.t_read_num;'
create_table_sql = 'show CREATE TABLE blog_log.t_read_num'


def main():
    mysql_executor = MysqlExecutor(host=host, port=port, user=user, passwd=passwd, db=db)
    column_count = mysql_executor.column_count(column_count_sql)

    select = mysql_executor.create_table_sql(create_table_sql)
    print(select)

    mysql_executor.close()


# main()
test = 'hello_world'
split = test.split("_")
for i in range(len(split)):
    split[i] = split[i].capitalize()

join = "".join(split)
print(join)
