# -*- coding: UTF-8 -*-
import pymysql


class MysqlExecutor:
    def __init__(self, host, port, user, passwd, db):
        print('初始化mysql连接. . .')
        self.conn = pymysql.connect(host=host, port=port, user=user, passwd=passwd, db=db)
        self.conn.set_charset("utf8")
        self.cursor = self.conn.cursor()

    def _do_execute(self, sql):
        cursor = self.cursor
        cursor.execute(sql)

        return cursor

    def column_count(self, sql):
        """获取表信息: 列数量"""
        return len(self._do_execute(sql).fetchall())

    def create_table_sql(self, sql):
        """获取表信息: 建表语句"""
        return self._do_execute(sql).fetchone()[1]

    def close(self):
        """关闭mysql连接"""
        self.cursor.close()
        self.conn.close()
        print('mysql 连接已经关闭. .')