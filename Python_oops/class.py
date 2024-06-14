class  Myclass:
    x=123

ref=Myclass()
print(type(ref))
#  ref  ->   stores  the address
print(ref,ref.x)

#----------------------------------------------------------------------------
#  __init__()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age


s_ref=student('koli',12)
print(s_ref,s_ref.name,s_ref.age)

#----------------------------------------------------------------------------
#__str__()

class student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return  f'name: {self.name} age:{self.age}'

s_ref=student('koli',12)
print(s_ref)
#-----------------------------------------------------------------------------
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John cena", 36)
p1.myfunc()

#-----------------------------------------------------------------------------
class   Dog:
   pass
dog_obj=Dog()
print(dog_obj)