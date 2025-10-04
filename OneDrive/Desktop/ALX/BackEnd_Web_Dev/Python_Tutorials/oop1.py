# Class Definition
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
# Create Function

    def bark(self):
        return f"{self.name} says Woof!"


# Object Creation
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "German Shepherd")
dog3 = Dog("Wendy", "Local ABK")
# Accessing Object Properties and Methods
print(f"{dog1.name} is a {dog1.breed}. {dog1.bark()}")
print(f"{dog2.name} is a {dog2.breed}. {dog2.bark()}")
print(f"{dog3.name} is a {dog3.breed}. {dog3.bark()}")


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass
# Inheritance


class Lion(Animal):
    def speak(self):
        return f"{self.name} the lion roars"


class Elephant(Animal):
    def speak(self):
        return f"{self.name} the lion trumpets"


# Polymorphism
zoo = [
    Lion("Simba"),
    Elephant("Dumbo")
]

for animal in zoo:
    print(animal.speak())
