class Animal(object):
    def run(self):
        print('animal is running')


class Dog(Animal):
    pass


dog = Dog()

dog.run()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
