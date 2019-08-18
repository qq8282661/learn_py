# 内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量
# 所以，不能用__name__、__score__这样的变量名
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量
# 不能通过instance.__name 去设置变量,
# 实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.__secret = name+str(score)

    def print_score(self):
        print('%s:%s' % (self.name, self.score))

    def print_grade(self):
        if self.score >= 90:
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return "C"

     # 除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入
    def max(self, score):
        if self.score > score:
            return self.score
        else:
            return score


john = Student("john", 80)
john.print_score()
print(john.print_grade())
print(john.max(79))
print(john._Student__secret)
