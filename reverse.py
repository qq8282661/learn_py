string = "I love you"
listStr = string.split(" ") 
print(listStr)
relist = listStr[-1::-1]
reStr = ' '.join(relist)
print(reStr)
