# -*- coding: UTF-8 -*-

mysql_2_java_type = {
    'bigint': 'Long',
    'binary': 'Byte[]',
    'bit': 'Byte[]',
    'blob': 'Byte[]',
    'tinyint': 'Integer',
    'char': 'String',
    'date': ['Date', 'java.util.Date'],
    'datetime': ['Timestamp', 'java.sql.Timestamp'],
    'decimal': ['BigDecimal', 'java.math.BigDecimal'],
    'double': 'Double',
    'enum': 'String',
    'float': 'String',
    'int': 'Integer',
    'longblob': 'Byte[]',
    'longtext': 'Byte[]',
    'mediumblob': 'Byte[]',
    'mediumint': 'Integer',
    'mediumtext': 'Byte[]',
    'set': 'String',
    'smallint': 'Integer',
    'text': 'Byte[]',
    'time': ['Time', 'java.sql.Time'],
    'timestamp': ['Timestamp', 'java.sql.Timestamp'],
    'tinyblob': 'Byte[]',
    'tinytext': 'Byte[]',
    'varbinary': 'Byte[]',
    'varchar': 'String',
    'year': ['Date', 'java.util.Date']
}

# 缩进,四个空格
retract = '    '
