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

    def get_columns(self, sql):
        """获取列信息"""
        return self._do_execute(sql).fetchall()

    def close(self):
        """关闭mysql连接"""
        self.cursor.close()
        self.conn.close()
        print('mysql 连接已经关闭. .')