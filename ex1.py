class Dog:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

dog_1 = Dog('Chow Chow')
print(dog_1.get_name())
dog_1.set_name('Chaw Chaw')
print(dog_1.get_name())