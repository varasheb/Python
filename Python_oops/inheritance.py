
# parent class
class person:
    def __init__(this,name,age,email):
        this.name=name
        this.age=age
        this.email=email

    def __str__(self) :
        return f"this is parent class person {self.name}"

person_obj=person('varshab',23,'exmaple@example.com')
print(person_obj,person_obj.name)

# child class
class employee(person):
    def __str__(self):
         return f"this is child class employee {self.name}"
    

employee_obj=employee('varshab',23,'exmaple@example.com')
print(employee_obj,employee_obj.name)
#-------------------------------------------------------------------------------------

# parent class
class person:
    def __init__(this,name):
        this.name=name
    def __str__(self) :
        return f"this is parent class person {self.name}"

person_obj=person('varshab')
print(person_obj,person_obj.name)

# child class
class employee(person):
    def __init__(this,name,age,email):
        this.name=name
        this.age=age
        this.email=email

    def __str__(self):
         return f"this is child class employee {self.name}"


employee_obj=employee('varshab',23,'exmaple@example.com')
print(employee_obj,employee_obj.name)

#-------------------------------------------------------------------------------------

#parent class
class Animal:
    def __init__(self,name,species) :
        self.name=name
        self.species=species
    
class Dog(Animal):
    def __init__(self, name, species, breed,gender):
        super().__init__(name, species)
        self.breed=breed
        self.gender=gender


animal_obj=Animal("kalu","order Carnivora")

dog_obj=Dog("kalu","order Carnivora","bull dog","Male")

if isinstance(dog_obj,Animal):
    print("dog object is child class of Animal")

#----------------------------------------------------------
# 2. Multiple Inheritance
# Multiple inheritance is when a class inherits from more than one parent class.


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Address:
    def __init__(self, address):
        self.address = address

class Student(Person, Address):
    def __init__(self, name, age, address, student_id):
        Person.__init__(self, name, age)
        Address.__init__(self, address)
        self.student_id = student_id

student = Student("Bob", 22, "123 Main St", "S67890")
print(student.name)  # Output: Bob
print(student.age)   # Output: 22
print(student.address) 
print(student.student_id)  

#---------------------------------------------------------------
# 3. Multilevel Inheritance
# Multilevel inheritance is when a class inherits from a class that inherits from another class.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

class CollegeStudent(Student):
    def __init__(self, name, age, student_id, major):
        super().__init__(name, age, student_id)
        self.major = major

college_student = CollegeStudent("varshab", 21, "S54321", "Computer Science")
print(college_student.name)  
print(college_student.age)   
print(college_student.student_id)  
print(college_student.major)  