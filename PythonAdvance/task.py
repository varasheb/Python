class Animal:
    pass

class dog(Animal):
    dog_name='dog'
    pass


class cat(Animal):
    cat_name='cat'
    pass


class pet(dog,cat):
    pass


if __name__=="__main__":
  pet_obj=pet()
  print(pet_obj.dog_name,pet_obj.cat_name)

print({i:i+2 for i in range(1,10) })

str="Hello World"
new_str=''
for word in str.split():
    new=''
    for i in word:
        new=i+new
    new=new+" "
    new_str+=new

print(new_str)

print(str[-1*len(str):-1*str.find(" ")])