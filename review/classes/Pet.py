class Pet:
    def __init__(self, name:str, age:int):
        self._name = name
        self._age = age
        # self.__collar = None

    def getName(self):
        return self._name

    def getAge(self):
        return self._age

    def setName(self, name:str):
        if isinstance(name, str):
            self._name = name

    def setAge(self, age:int):
        if isinstance(age, int):
            self._age = age

    def speak(self):
        pass

    def __str__(self):
        return f"{self._name} is a {self.__class__.__name__} of {self._age} years old"


if __name__ == '__main__':
    my_pet = Pet("Balto", 4)
    print(my_pet.getName())
    print(my_pet.getAge())
    print(my_pet)

