from Pet import Pet

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)

    def speak(self):
        print("Ruff")


if __name__ == '__main__':
    myDog = Dog("Champ", 2)
    myDog.setName("Champ II")
    print(myDog.getName())
    myDog.speak()