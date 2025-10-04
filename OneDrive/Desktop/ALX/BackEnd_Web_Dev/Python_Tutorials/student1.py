# Class Definition
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass
    # Function definition

    def response(self):
        return f"{self.name}, yes sir!"


    # Object Creation
student1 = Student("Richard Amoah", "21 years old")
student2 = Student("Wendy Sam", "19 years old")
# Accessing Object Attributes and Methods
print(f"{student1.name} is {student1.age}. {student1.response()}")
print(f"{student2.name} is {student2.age}. {student2.response()}")
