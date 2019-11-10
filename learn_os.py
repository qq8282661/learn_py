import os

'''
文件操作和目录
'''
# 查看系统环境变量
print(os.environ)

print('PATH', os.environ.get('PATH'))

# 查看当前目录的绝对路径:
print('path', os.path.abspath('.'))

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
abspath = os.path.join(os.path.abspath('.'), 'test_dir')
print('abspath', abspath)

# 创建文件夹如果有会报错，rmdir也会报错
# os.mkdir(abspath)
# os.rmdir(abspath)
# os.path.splitext()可以直接让你得到文件扩展名
# 而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名
# 重命名文件：os.rename('test.txt', 'test.py')，删除文件：os.remove('test.py')

directory = [x for x in os.listdir('.') if os.path.isdir(x)]
print(directory)

pythonFile = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']

print(pythonFile)
