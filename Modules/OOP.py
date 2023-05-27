class Animal: 
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):#Inheretance
    def purr(self):
        print("Purr...")
        
class Dog(Animal):
    def bark(self):
        print("Woof!")

class horn():
    def voice(self):
        print("VOICEOOO\a\a\a")
        
class A:
    def spam(self):
        print(1)

class B(A):
    def spam(self):
        print(2)
        super().spam()
"""
The function super is a useful inheritance-related function that 
refers to the parent class. It can be used to find the method 
with a certain name in an object's superclass.
"""

class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    #Magic methods
    #They are also known as dunders.
    #They are used to create functionality that can't be represented as a normal method.
"""
More magic methods for common operators:
__sub__ for -
__mul__ for *
__truediv__ for /
__floordiv__ for //
__mod__ for %
__pow__ for **
__and__ for &
__xor__ for ^
__or__ for |
"""

class SpecialString:
    def __init__(self, cont):
        self.cont = cont

    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
    
    def __gt__(self, other):
        for index in range(len(other.cont)+1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)


"""
Python also provides magic methods for comparisons.
__lt__ for <
__le__ for <=
__eq__ for ==
__ne__ for !=
__gt__ for >
__ge__ for >=

If __ne__ is not implemented, it returns the opposite of __eq__.
There are no other relationships between the other operators.
"""

import random

class VagueList:
    def __init__(self, cont):
        self.cont = cont

    def __getitem__(self, index):
        return self.cont[index + random.randint(-1, 1)]

    def __len__(self):
        return random.randint(0, len(self.cont)*2)

"""
There are several magic methods for making classes act like containers.
__len__ for len()
__getitem__ for indexing
__setitem__ for assigning to indexed values
__delitem__ for deleting indexed values
__iter__ for iteration over objects (e.g., in for loops)
__contains__ for in

There are many other magic methods that we won't cover here, such as __call__ for calling objects as functions, and __int__, __str__, and the like, for converting objects to built-in types.
"""

class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)

    def push(self, value):
        self._hiddenlist.insert(0, value)

    def pop(self):
        return self._hiddenlist.pop(-1)

    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
    #The __repr__ magic method is used for string representation of the instance.

class Spam:
    __egg = 7
    def print_egg(self):
        print(self.__egg)

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    @classmethod
    def new_square(cls, side_length):
        return cls(side_length, side_length)

class Person:
    def __init__(self, name):
        self.name = name
    
    @classmethod
    def sayHi(cls):    
        print("Hi")

class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings

    @staticmethod
    def validate_topping(topping):
        if topping == "pineapple":
            raise ValueError("No pineapples!")
        else:
            return True

    @property
    def pineapple_allowed(self):
        return False

"""
What is the difference between a class method and a static method?
Class methods are passed the calling class, static methods aren't
"""

class Pizza2:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineapple_allowed = False

    @property
    def pineapple_allowed(self):
        return self._pineapple_allowed

    @pineapple_allowed.setter
    def pineapple_allowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "123":
                self._pineapple_allowed = value
            else:
                raise ValueError("Alert! Intruder!")



def printLine():
    print(8*"\|/")
        
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)

print(felix.color)

printLine()

fido = Dog("Fido", "brown")
print(fido.name)
fido.bark()

printLine()

#If a class inherits from another with the same attributes or methods, it overrides them.

printLine()

horn().voice()
#you can call methods using the class name

printLine()

B().spam()

printLine()

first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second#The expression x + y is translated into x.__add__(y).
#However, if x hasn't implemented __add__, and x and y are of different types, then y.__radd__(x) is called.
print(result.x)
print(result.y)

printLine()

spam = SpecialString("spam")
hello = SpecialString("Hello world!")
print(spam / hello)

printLine()

spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs

printLine()

vague_list = VagueList(["A", "B", "C", "D", "E"])
print(len(vague_list))
print(len(vague_list))
print(vague_list[2])
print(vague_list[2])

printLine()

queue = Queue([1, 2, 3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)

printLine()

s = Spam()
s.print_egg()
print(s._Spam__egg)
#Basically, Python protects those members by internally changing the name to include the class name.
#print(s.__egg)#Error

printLine()

square = Rectangle.new_square(5)
print(square.calculate_area())

printLine()

pizza = Pizza(["cheese", "tomato"])
print(pizza.pineapple_allowed)
#pizza.pineapple_allowed = True#Error
#can't set attribute now this attribute is readonly

printLine()

pizza = Pizza2(["cheese", "tomato"])
print(pizza.pineapple_allowed)
pizza.pineapple_allowed = True
print(pizza.pineapple_allowed)

printLine()

        