#Lab 1

# Python Intro:
print("Hello World!")

# Python User Input:
name = input("Enter your name: ")
print(f"Hello, {name}")

# Python Get Started:
print("Welcome to Python")

# Python Syntax:
if 5 > 2:
    print("5 is greater than 2")

# Python Comments:
# This is first way of commenting
'''This is second way of
commentin with more than 1 line'''

# Python Variables:
x = 5
y = "Python"

# Python Data Types:
x = 5   #integer
y = "Ohh"   #string
z = 3.0   #float
w = True   #boolean(also we have False)

# Python Numbers:
x = 5
y = 3
print(x + y)  # Addition
print(x - y)  # Subtraction
print(x * y)  # Multiplication
print(x / y)  # Division

# Python Casting:
x = int(9.5) # float to int
y = str(156) # int to string

# Python Strings:
txt = "Hello"
print(txt[2])
print(txt.upper)
print(txt.lower)
print(lex(txt))

# Python String Formatting:
name = "Sayat"
age = 18
print(f"My name is {name}, and I am {age} years old.")

# Python Booleans:
print(5 > 2) # it gives True
pritn(5 < 2) # it gives False

# Python Operators:
x = 5
y = 2
print(x + y)  # Arithmetic
print(x > y)  # Comparison
print(x * y)  # Multiplication
print(x ** y) # POWER!
print(x % y) # Moduls
print(x > 0 and y > 0)  # Logical
print(x is y) # Identity
print(x is not y) # Identity
print(x in y) # Membership
print(x & y) # Bitwise


# Python If...Else:
x = 5
if x > 2:
    print("x is greater than 2")
else:
    print("x is less than or equal to 5")


# Git
'''
These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   restore    Restore working tree files
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   diff       Show changes between commits, commit and working tree, etc
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   backfill   Download missing objects in a partial clone
   branch     List, create, or delete branches
   commit     Record changes to the repository
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   reset      Reset current HEAD to the specified state
   switch     Switch branches
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects
'''