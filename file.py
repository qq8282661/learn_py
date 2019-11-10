# 调用read()会一次性读取文件的全部内容，如果文件有10G，内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
# 每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，调用readlines()一次读取所有内容并按行返回list
with open('./requirements.txt', "r") as f:
    print(f.read())
    lines = f.readlines();
    print('lines', lines)
    for line in f.readlines():
        print('line', line)
        print(line.strip())
# file-like Object:file-like Object不要求从特定类继承，只要写个read()方法就行。
# 二进制文件：用'rb'模式打开文件即可 #默认16进制表示
with open('./basics/eg.jpg', 'rb') as f:
    print(f.read())
# 字符编码 给open()函数传入encoding参数
'''
 f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')
 f.read()
'''
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
f = open('./test.txt', 'w')
f.write('hello world')
f.close()
# 忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。所以，还是用with语句来得保险：
with open('test.txt', 'w') as w:
    w.write('new world')
# 给open()函数传入encoding参数，将字符串自动转换成指定编码。以'w'模式写入文件时，如果文件已存在
# ，会直接覆盖'a'以追加（append）模式写入

