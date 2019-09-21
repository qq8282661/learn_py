# 对类的属性进行控制


class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定属性的名称
