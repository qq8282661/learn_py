class Hello(object):
    pass


# type()函数可以查看一个类型或变量的类型
# https://www.liaoxuefeng.com/wiki/1016959663602400/1017592449371072
s = Hello()
print(type(s))
print((type(Hello)))


# metaclass:先定义metaclass，就可以创建类，最后创建实例。
# metaclass是类的模板，所以必须从`type`类型派生：

class ListMetaclass(type):
    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)


class MyList(list, metaclass=ListMetaclass):
    pass


L = MyList()
L.add(1)
print(L)
