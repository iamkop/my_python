class People:
    def print_default(self):
        print("姓名: ", self.name, " 年龄: ", self.age)

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def your_test(self, f):
        pass

    def get_name(self):
        return self.__name

func = lambda :print("----")

p = People("li", 25)
p.your_test((lambda : print(p.get_name()))())
