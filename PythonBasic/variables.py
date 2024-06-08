# python variables

x=1
print(type(x))

x=1.1
print(type(x))

x='A'
print(type(x))

x='varshab'
print(type(x))

x=True
print(type(x))

x=False
print(type(x))

x=1010
print(type(x))

a, b, c = "Orange", "Banana", "Cherry"
print(a)
print(b)
print(c)

#unpack
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

x = 5
y = "John"
#print(x+y)  # type error
print(y,x)

p = "awesome hana"

def myfunc():
  print("Python is " + p)

myfunc()

xp= "awesome"

def myfunc():
  xp = "fantastic"
  print("Python is " + xp)

myfunc()

print("Python is " + xp)
print('-----------------------------------')
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)