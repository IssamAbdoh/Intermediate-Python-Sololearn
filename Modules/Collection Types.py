counter=0
def PrintALine() :
    global counter
    # refer to global variable 'counter' inside function
    counter+=1
    print( 8*"\/" + " " + str(counter) )

#Lists are one of these collection types, and they allow you to store indexed values:

#Dictionaries can be indexed in the same way as lists, using square brackets containing keys.
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])

PrintALine()

"""
Only immutable objects can be used as keys to dictionaries. 
Immutable objects are those that can't be changed.
So far, 
the only mutable objects you've come across are lists 
and dictionaries.
"""

bad_dict = {
    #[1, 2, 3]: "one two three", 
}
#Since lists are mutable, the code above throws an error.

bad_dict[1]=1
bad_dict["issam"]=456
print(bad_dict[1])
print(bad_dict["issam"])

PrintALine()

nums = {
    1: "one",
    2: "two",
    3: "three",
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)

PrintALine()

pairs = {1: "apple",
  "orange": [2, 3, 4], 
  True: False, 
  12: "True",
}

print(pairs.get("orange"))
print(pairs.get(7, 42))
print(pairs.get(12345, "not found"))
print(pairs[True])
print(pairs[1])
print(len(pairs))

PrintALine()

words = ("spam", "eggs", "sausages",)
print(words[0])
#Trying to reassign a value in a tuple causes an error.
#words[1] = "cheese"
#Like lists and dictionaries, tuples can be nested within each other.

PrintALine()

#Tuples can be created without the parentheses by just separating the values with commas.
my_tuple = "one", "two", "three"
print(my_tuple[0])
#Tuples are faster than lists, but they cannot be changed.

PrintALine()

numbers = (1, 2, 3)
#Tuple unpacking
a, b, c = numbers
print(a)
print(b)
print(c)
#This can be also used to swap variables by doing a, b = b, a , since b, a on the right hand side forms the tuple (b, a) which is then unpacked.

PrintALine()

a = 1 ; b= 2 ; c = 3
a , b = b , a
print(a,b,c)

PrintALine()

#A variable that is prefaced with an asterisk (*) 
#takes all values from the collection that are left over 
#from the other variables.
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)#c will get assigned the values 3 to 8.
print(d)

PrintALine()

"""
Sets are similar to lists or dictionaries.
They are created using curly braces, and are unordered, which means that they can't be indexed.

Due to the way they're stored, it's faster to check whether an item is part of a set using the in operator, rather than part of a list.
"""
num_set = {1, 2, 3, 4, 5}

print(3 in num_set)
#Sets cannot contain duplicate elements.

PrintALine()

nums = {1, 2, 1, 3, 1, 4, 5, 6}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
print(len(nums))

PrintALine()

"""
Sets can be combined using mathematical operations.
The union operator | combines two sets to form a new one containing items in either.
The intersection operator & gets items only in both.
The difference operator - gets items in the first set but not in the second.
The symmetric difference operator ^ gets items in either set, but not both.
"""
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}

print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)

PrintALine()

# a list comprehension
cubes = [i**3 for i in range(5)]

print(cubes)

PrintALine()

#A list comprehension can also contain an if statement to enforce a condition on values in the list.
evens=[i**2 for i in range(10) if i**2 % 2 == 0]

print(evens)

PrintALine()

"""
Data Structures

As we have seen in the previous lessons, Python supports the following collection types: Lists, Dictionaries, Tuples, Sets.

When to use a dictionary:
- When you need a logical association between a key:value pair.
- When you need fast lookup for your data, based on a custom key.
- When your data is being constantly modified. Remember, dictionaries are mutable.

When to use the other types:
- Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
- Use a set if you need uniqueness for the elements.
- Use tuples when your data cannot/should not change.

***Many times, a tuple is used in 
combination with a dictionary, 
for example, a tuple might represent a key, 
because it's immutable.
"""

my_tuple = ('a', 'b', 'c', 'd')
print(my_tuple[1:]) #Print elements from index 1 to end
print(my_tuple[:2]) #Print elements from start to index 2
print(my_tuple[1:3]) #Print elements from index 1 to index 3
print(my_tuple[::2]) #Print elements from start to end using step sizes of 2
#immutable means that you cannot change the value of its elemnts,
#but you can overwrite the value of itself 

PrintALine()

text = input()
dict = {}
#your code goes here
for letter in text :
    if letter not in dict:
        dict[letter]=1
    else :
        dict[letter]+=1

print(dict)

PrintALine()

