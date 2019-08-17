class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

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
