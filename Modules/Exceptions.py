"""
Exceptions


Different exceptions are raised for different reasons.
Common exceptions:
ImportError: an import fails;
IndexError: a list is indexed with an out-of-range number;
NameError: an unknown variable is used;
SyntaxError: the code can't be parsed properly;
TypeError: a function is called on a value of an inappropriate type;
ValueError: a function is called on a value of the correct type, but with an inappropriate value.
Python has several other built-in exceptions, such as ZeroDivisionError and OSError. Third-party libraries also often define their own exceptions.
"""

try:
    num1 = 7
    num2 = 0
    print (num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occurred")
    print("due to zero division")
    
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")
    
try:
    print("Hello")
    print(1 / 0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("This code will run no matter what")
    
#The finally block is useful, for example, when working with files and resources: it can be used to make sure files or resources are closed or released regardless of whether an exception occurs.

try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)

try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)

"""
num = 102
if num > 100:
  raise ValueError
"""

"""
The following code will result in two exceptions
try:
    print(1 / 0)
except ZeroDivisionError:
    raise ValueError
"""

"""
name = "123"
raise NameError("Invalid name!")
"""

x = 0
try:
  x+=1
  raise ValueError
except NameError:
  x+=1
except ValueError:
  x+=1
else:
  x+=1
finally:
  x+=1  
  print("The value of x is {x}".format(x=x))

try:
    name = input()
    #your code goes here
    if len(name)<4:
        raise ValueError

except ValueError:
    print("Invalid Name")

else:
    print("Account Created")
