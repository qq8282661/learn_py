import types

print(type(123) == type(123))
print(type(1) == str)


def fc():
    pass


print(type(fc) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type((x for x in range(10))) == types.GeneratorType)

# 使用instance()判断类型

# 使用dir() 如果要获得一个对象的所有属性和方法，可以使用dir()函数
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：
print(dir('ABC'))
# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：


class MyDog(object):
    def __len__(self):
        return 100


dog = MyDog()
print(dog.__len__())

# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：
