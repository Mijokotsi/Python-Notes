import random

print("Hello World, this is my first code in python")

# Setting a range in a variable and printing the consisting number
x = range(6)
for i in x:
    print(i)

# Defining a tuple
tuple = {1, 2, 3, 5, 6, "Apple"}
for i in tuple:
    print(i)

# complex numbers cannot be typecasted
complex = 1+5j
print(complex)

# Prints any random number form the given range i.e., 1 - 10
r = random.randrange(1, 10)
print(r)

# We can directly loop through a string without specifying its length
string = "banana"
for i in string:
    print(i)

length = len(string)
print(length)


str = "ahbgdc"
sub = "abc"

print(sub in str)    # This works for subset, not subsequence
print(sub not in str)


# String slicing
str1 = "Hello World"

# In each slicing syntax num1:num2, num1 position is included, but num2 isn't
print(str1[2:5])
print(str1[2:])
print(str1[:7])
print(str1[-5:-2])   # Negative indexing is used to access the string from the backward direction

# String modifying techniques
mod = " Hello, World, I'm, Snehil, Seenu!"
print(mod.upper())
print(mod.lower())
print(mod.split(","))   # This will split the string from wherever there is a comma, and turn it into a list
print(mod.strip())   # This method will remove the white spaces from the string (if any) from the beginning and end
print(mod.replace("H", "W"))    # Replaces the string characters


# Concatenate string and numbers using format() method
num = 21
txt = "Hi this is my 2nd day of learning python, and I'm {} yrs old"    # {} is called placeholders
print(txt.format(num))    # format() method can have unlimited no. of arguments

item = 8
price = 768.50
dist = 10
# We can also place indexes in th placeholders to put the values as per out need
# indexes are based as variables are defined as the arguments in the txt1 string
txt1 = "I came from Michigan which is {1} kms from this shop and I've bought {0} items and need to pay {2} dollars"
print(txt1.format(item, dist, price))

# Empty string, 0 in number, and the value None represents false in boolean
print(bool(""))
print(bool())
print(bool(None))
