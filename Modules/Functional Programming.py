
counter=0
def PrintLine() :
    global counter
    # refer to global variable 'counter' inside function
    counter+=1
    print( 15*"/|\\" + " " + str(counter) )

PrintLine()

"""
Higher-order functions take other functions as arguments, or return them as results
"""

def apply_twice(func, arg):
    return func(func(arg))

def add_five(x):
    return x + 5

print(apply_twice(add_five, 10))

PrintLine()

#Pure functions have no side effects, and return a value that depends only on their arguments.

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

some_list = []
def impure(arg):
  some_list.append(arg)

"""
Using pure functions has both advantages and disadvantages.
Pure functions are:
- easier to reason about and test.
- more efficient. Once the function has been evaluated for an input, the result can be stored and referred to the next time the function of that input is needed, reducing the number of times the function is called. This is called memoization.
- easier to run in parallel.
"""

PrintLine()

def my_func(f, arg):
  return f(arg)

print(my_func(lambda x: 2*x*x, 5))

#Functions created using the lambda syntax are known as anonymous.

#named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))

#lambda
print((lambda x: x**2 + 5*x + 4) (-4))

PrintLine()

def add_five(x):
    return x + 5

nums = [11, 22, 33, 44, 55]
result = list(map(add_five, nums))
print(result)

#We could have achieved the same result more easily by using lambda syntax.

nums = [11, 22, 33, 44, 55]

result = list(map(lambda x: x+5, nums))
print(result)

PrintLine()

nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x%2==0, nums))
print(res)

PrintLine()

def countdown():
    i=5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)
"""
Generators are a type of iterable, like lists or tuples.
Unlike lists, they don't allow indexing with arbitrary indices, but they can still be iterated through with for loops.
They can be created using functions and the yield statement.
    
The yield statement is used to define a generator, replacing the return of a function to provide a result to its caller without destroying local variables.

In short, generators allow you to declare a function that behaves like an iterator, i.e. it can be used in a for loop.
"""
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i

print(list(numbers(11)))

"""
Using generators results in improved performance, 
which is the result of the lazy (on demand) generation of values, 
which translates to lower memory usage. Furthermore, 
we do not need to wait until all the elements have been generated 
before we start to use them.
"""

PrintLine()

def decor(func):
    def wrap():
        print("============")
        func()
        print("============")
    return wrap

def print_text():
    print("Hello world!")

decorated = decor(print_text)
decorated()

#We could say that the variable decorated is a decorated version of print_text -- it's print_text plus something.

"""
In fact, if we wrote a useful decorator we might want to replace print_text with the decorated version altogether so we always got our "plus something" version of print_text.
This is done by re-assigning the variable that contains our function:
"""
print_text = decor(print_text)
print_text()
print()
print_text = decor(print_text)
print_text = decor(print_text)
print_text = decor(print_text)
print_text()

PrintLine()

#This will have the same result as the above code.

def decora(func):
    def wrap():
        print("=a=a=a=a=a=a=a=a=a=a=a=")
        func()
        print("=a=a=a=a=a=a=a=a=a=a=a=")
    return wrap

@decora
def print_textooo():
    print("Hello world!")

print_textooo();
#A single function can have multiple decorators.

PrintLine()

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)


print(is_odd(17))
print(is_even(23))

PrintLine()


def function(named_arg, *args):
    print(named_arg)
    print(args)#args now is a tuple

function(1, 2, 3, 4, 5)

PrintLine()


def my_func(x, y=7, *args, **kwargs):
    print(kwargs)#dictionary filled with named arguments
#The arguments returned by **kwargs are not included in *args.

my_func(2, 3, 4, 5, 6, a=7, b=8)

def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)

PrintLine()

def spell(txt):
    #your code goes here
    if len(txt)==1:
        print(txt)
    else:
        print(txt[-1])
        spell(txt[:-1:1])
    

txt = input("input any text to spell it backward")
spell(txt)
