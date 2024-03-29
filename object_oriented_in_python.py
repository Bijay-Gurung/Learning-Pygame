# -*- coding: utf-8 -*-
"""Object Oriented In Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LMyWWUb1K467oQxdff89JajvS4oMau6b

Classes : It is a blueprint of an object.

Object: It is the member or Instances of a class.
"""

class person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

p1 = person("Bijay",19)

print(p1.name)
print(p1.age)

# Object Methods

class Animal:
  def __init__(self,name,color):
    self.name = name
    self.color = color

  def sound(self):
    print(f"{self.name} makes Sound.")

p1 = Animal("Dog","Black")
p1.sound()

# Modifying object properties
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"My name is {self.name}.\nI am {self.age} years old.")

p1 = Person("Karma",20)
p1.age = 19
p1.myfunc()

# Delete Object Properties
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"My name is {self.name}.\nI am {self.age} years old.")

p1 = Person("Karma",20)
del p1.age
p1.age

# delete object
class Person:
  def __init__(self,name,age):
    self.name = name
    self.age = age

  def myfunc(self):
    print(f"My name is {self.name}.\nI am {self.age} years old.")

p1 = Person("Karma",20)
del p1
print(p1)

# Pass statement to avoid getting an error
class empty:
  pass

"""Inheritance: It is a pillar of object oriented where properties and methods can be shared or extended."""

# parent class
class person:
  def __init__(self,firstName,lastName):
    self.firstName = firstName
    self.lastName = lastName

  def printName(self):
    print(self.firstName, self.lastName)

x = person("Karma","Gurung")
x.printName()

# child class extended from parent class (person)
class student(person):
  pass # Use the pass keyword when we do not want to add any other properties or methods to the class.

  # Now the student class (child) also has the same properties  and methods as the person class (parent).
x1 = student("Bijay","Gurung")
x1.printName()

"""Adding the __init__() function in child class"""

class student(person):
  def __init__(self,firstName,lastName):
    """
    when we add the __init__() function to the child class.
    the class will no longer inherit the parent's __init__() function.
    The child's __init__() function overrides the inheritance of the parent's __init__() function.
    """
    person.__init__(self,firstName,lastName)
    """
    To keep the inheritance of the parent's __init__() function, we have to call the parent's __init__()
    function in child __init__() function.
    """
  x = student("Dolma","Ghale")
  x.printName()

"""Super() function: It will make the child class inherit all the methods and properties from it's parent class."""

class student(person):
  def __init__(self,firstName,lastName):
    super().__init__(firstName,lastName)

x = student("Mohan","Gurung")
x.printName()

# Adding properties to the student class (child)

class student(person):
  def __init__(self,firstName,lastName):
    super().__init__(firstName,lastName)
    self.graduationYear = 2026

x = student("Maya","Ghale")
x.graduationYear

# Another variation
class student(person):
  def __init__(self,firstName,lastName,year):
    super().__init__(firstName,lastName)
    self.graduationYear = year

x = student("Maya","Ghale",2019)
x.graduationYear

# Adding Methods in student class (child)
class student(person):
  def __init__(self,firstName,lastName):
    super().__init__(firstName,lastName)

  def welcome(self):
    print(f"Welcome {self.firstName} {self.lastName}")

x = student("Sonam","Kapoor")
x.welcome()

"""Polymorphism: It is the same method or property that can behave differently in different context.


There are two types of polymorphism:
1. Method Overloading
2. Method Overriding
"""

# polymorphism is often used in class methods, where we can have multiple classes with the same method name.

class car:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class boat:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class plane:
  def __init__(self,brand,model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = car("Ford","Mustang")
boat1 = boat("Ibiza","Touring 20")
plane1 = plane("Boeing","747")

for x in (car1,boat1,plane1):
  x.move()

# Inherit class polymorphism
class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail!") # method overriding

class Plane(Vehicle):
  def move(self):
    print("Fly!") # method overriding

car1 = Car("Ford", "Mustang") #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()