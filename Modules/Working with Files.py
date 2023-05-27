def printLine():
    print(9*"/|\\")

printLine()

"""
You can specify the mode used to open a file by applying a second argument to the open function.
Sending "r" means open in read mode, which is the default.
Sending "w" means write mode, for rewriting the contents of a file.
Sending "a" means append mode, for adding new content to the end of the file.

Adding "b" to a mode opens it in binary mode, which is used for non-text files (such as image and sound files).
"""

"""
# write mode
open("files/filename.txt", "w")

# read mode
open("files/filename.txt", "r")
open("files/filename.txt")

# binary write mode
open("files/filename.txt", "wb")

"""

"""
You can combine modes, 
for example, 
wb from the code above opens the file in binarywrite mode.
"""

"""
file = open("files/filename.txt", "w")
# do stuff to the file
file.close()
"""

"""
How would you close a file stored in a variable "text_file"?
text_file.close()
"""

file = open("files/filename.txt", "r")
txt =file.read()
print(txt)
file.close()

printLine()

"""
To read only a certain amount of a file, you can provide the number of bytes to read as an argument to the read function.
Each ASCII character is 1 byte:
"""
file = open("files/filename.txt", "r")
print(file.read(5))#reads 5 characters , the curser is on the sixth character now
print(file.read(7))#reads more 7 characters  , starting from the 6th to 13th , the curser is on the 13th character now
print(file.read())#reads the rest of the file , starting from 13th to the end of the file
file.close()
"""
This will read the first 5 characters of the file, then the next 7.
Calling the read() method without an argument will return the rest of the file content.
"""

printLine()

file=open("files/filename.txt", "r")
x = file.readlines()
for line in x:
    print(line)
    
print(x) 
file.close()

printLine()

"""
If you do not need the list for each line, you can simply iterate over the file variable:
"""
file=open("files/filename.txt", "r")
for line in file:
    print(line)
    
file.close()

printLine()

file = open("files/newfile.txt", "w")
file.write("This has been written to a file")
file.close()

file = open("files/newfile.txt", "r")
print(file.read())
file.close()

printLine()

file = open("files/newfile.txt", "a")#"a" stands for append or add

file.write("\nThe Da Vinci Code")
file.close()

file = open("files/newfile.txt", "r")
print(file.read())
file.close()

printLine()

#The write method returns the number of bytes written to a file, if successful.

file = open("files/newfile.txt", "w")
amount_written = file.write("koko")
print(amount_written)
file.close()

#To write something other than a string, it needs to be converted to a string first.

printLine()

"""
It is good practice to avoid wasting resources by making sure that files are always closed after they have been used. One way of doing this is to use try and finally
"""
file = open("Files/books.txt","w")
file.write("Hakuna matata")
file.close()
try:
    f = open("Files/books.txt")
    cont = f.read()
    print(cont)
except:
    print("an error has occured !")
finally:
    f.close()

printLine()

"""
An alternative way of doing this is by using with statements.
This creates a temporary variable (often called f), 
which is only accessible in the indented block of the with statement.
"""
with open("files/books.txt") as f :
    print(f.read())
#The file is automatically closed at the end of the with statement, 
#even if exceptions occur within it.

printLine()

"""
a code that prints the first letters compined for each word in a line
in other way :
for each line prints the first letter of each word in this line
"""
file = open("files/newfile.txt", "r")

#your code goes here
for line in file.readlines():
    words = line.split(" ")
    ans = ""
    for word in words:
        ans+=word[0]
    print(ans)

file.close()
