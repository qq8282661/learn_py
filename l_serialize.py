import pickle
import json

# 序列化
d = dict(name='Bob', age=20, score='80')

print(pickle.dumps(d))

with open('dump.txt', 'wb') as f:
    pickle.dump(d, f)

with open('dump.txt', 'rb') as r:
    rd = pickle.load(r)

print(rd)

# 字典转json dumps s--string
j = json.dumps(d)
print(j)

jd = json.loads(j)
print(jd)


# 序列化class
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s = Student('Bob', 20, 88)

js = json.dumps(s, default=lambda obj: obj.__dict__)
print(js)


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


rs = json.loads(js, object_hook=dict2student)
print(rs)

# 上传远程测试
