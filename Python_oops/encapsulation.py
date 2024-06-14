class Student:
    def __init__(self, name, age):
        self.__name = name  
        self.__age = age   

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age cannot be negative")


student = Student("varshab", 23)

print(student.get_name())  
student.set_age(21)
print(student.get_age())   
student.set_age(-5)       
