# -*- coding: UTF-8 -*-

import mysql2javapo.constant as constant
import datetime

def _build_blank_line():
    """ 写空格行 """
    return '\n'


def build_class_content(columns):
    """ 写类中的内容,import信息,参数(列格式): [[name1,type1,comment2],[name2 ...]] """
    return ''


def build_po(package_name, columns):
    """ 构建类po对象 """
    package_info = 'package {package_name};\n\n'.format(package_name=package_name)
    import_info = ''
    class_doc = ''
    class_structure = '{0}{1}{2}public class Test {{\n{3}\n}}'
    class_structure.format(package_info, import_info, class_doc, build_class_content(columns))
    return class_structure


class JavaFileWriter:
    def __init__(self, path, encoding, package_name, columns):
        """ 列格式: [[name1,type1,comment2],[name2 ...]] """
        self.columns = columns
        self.package_info = 'package {package_name};\n\n'.format(package_name=package_name)
        self.import_info = ''
        self.class_doc = '/**\n * @author userName\n * @date {time}' \
                         '\n * @Description todo(用一句话描述该文件做什么)\n */'\
            .format(time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                                                                       )
        self.class_structure = '{0}{1}{2}public class Test {{\n{3}\n}}'
        # with open(path, 'w', encoding=encoding) as w:
        #     w.write(build_po(package_name, columns))

    def build_class(self):
        """ 构建类 """
        print(self.class_doc)
        for column in self.columns:
            # print(column)
            pass

    # @staticmethod
    # def write_class():
    #     print("---")
    #     pass
