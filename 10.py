#inheritance example
class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
class Dog(Animal):
    def speak(self):
        return"woof"
class Cat(Animal):
    def speak(self):
        return "meow"
dog=Dog("buddy")
cat=Cat("whiskers")

print(dog.name, dog.speak())
print(cat.name, cat.speak())