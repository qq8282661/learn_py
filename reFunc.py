def createCounter():
    l = 0

    def counter():
        l = l+1
        return l
    return counter


counterA = createCounter()
print(counterA())
print(counterA())
