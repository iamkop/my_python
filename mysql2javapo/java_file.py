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
    def __init__(self, encoding, package_name, columns):
        """ 列格式: [[name1,type1,comment2],[name2 ...]] """
        self.encoding = encoding
        self.columns = columns
        self.package_info = 'package {package_name};'.format(package_name=package_name)
        self.import_info = []
        self.class_doc = '\n\n/**\n * @author ${{userName}}\n * @date {time}' \
                         '\n * @Description ${{todo}}(用一句话描述该文件做什么)\n */\n' \
            .format(time=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    )
        self.class_structure = '{0}{1}{2}public class Test {{{3}{4}\n}}'

    def build_field_import(self):
        """ 构建类的字段 """
        fields = []
        get_set = []
        # 循环处理
        for column in self.columns:
            column_name = column[0]
            column_type = column[1]
            column_common = column[2]
            java_type = constant.mysql_2_java_type[column_type]
            retract = constant.retract
            # 是否需要import java 包,如果需要
            if isinstance(java_type, list):
                java_type_real = java_type[0]
                import_this = 'import ' + java_type[1] + ';'
                if import_this not in self.import_info:
                    self.import_info.append('import ' + java_type[1] + ';')
            # 如果不需要
            else:
                java_type_real = java_type
            # 下划线分隔变为驼峰写法
            column_split = column_name.split('_')
            column_final_name = ''
            for column_script in column_split:
                # 第一个单词不首字母大写
                if column_split.index(column_script) > 0:
                    column_final_name += column_script.capitalize()
                else:
                    column_final_name += column_script
            fields.append('\n\n' + retract + '/** {common} */\n'.format(common=column_common) \
                          + retract + 'private ' + java_type_real + ' ' + column_final_name + ';')
            # 方法名需要首字母大写(紧跟get or set 后的首字母)
            column_for_get_set = ''.join(map(lambda x: x.capitalize(), column_name.split('_')))
            # get 方法的模板
            get_temp = '\n\n    public {field_type} get{field_name_ca}() {{\n        return {field_name};\n    }}'
            # set 方法的模板
            set_temp = '\n\n    public void set{field_name_ca}({java_type_real} {field_name})' \
                       ' {{\n        this.{field_name} = {field_name};\n    }}'
            get_set.append(get_temp.format(field_type=java_type_real, field_name_ca=column_for_get_set
                                           , field_name=column_final_name))
            get_set.append(set_temp.format(field_name_ca=column_for_get_set, field_name=column_final_name
                                           ,java_type_real=java_type_real))
        return {'fields': fields, 'get_set': get_set}

    def write_class(self, path):
        """ 写类文件 """
        field_list = self.build_field_import()
        fields = ''.join(field_list['fields'])
        get_set = ''.join(field_list['get_set'])
        imports = ''
        if len(self.import_info) > 0:
            imports = '\n\n' + '\n'.join(self.import_info)

        with open(path, 'w', encoding=self.encoding) as w:
            w.write(self.class_structure.format(self.package_info, imports, self.class_doc, fields, get_set))
