print("hello world")

# This is an if else block
if 5 > 3:
    print("This is correct")
else:
    print("This is wrong")

string = """ This is a multiline string,
and this is the first time I'm using it
in any python code """
print(string)

a = 9
b = float(4)  # This is called variable casting
c = True

print(type(a))  # This is the method to get the type of any variable
print(b)
print(type(c))

# Assigning multiple values to multiple variables at the same time
x, y, z = "Apple", "mango", "Banana"
print(x)
print(y)
print(z)

# Following technique is called unpacking
fruits = ["Apple", "Mango", "Banana"]
x, y, z = fruits

print(x)
print(y)
print(z)

# Methods of Printing multiple values at once, that too in a single line
print(x, y, z)  # Best way to print multiple values together
print(x + y + z)  # Here, the variable values will be printed as stick to each other like AppleMangoBanana

# When you define the global and local variable with the same name,
# inside function only the local variable wil be used
p = "learning Python"


def fun():
    p = "Snehil is "
    print(p + p)  # Only Snehil is string working


fun()
print(p)  # Here the global variable will run

# Making a variable global inside a function, and using it outside the function
def first():
    global x
    x = "fantastic"
    print("I'm " + x)

first()
print(x)

# We can also change the value of global values by using global keyword elsewhere in the code
abc = "Old global"
def changeGlobal():
    global abc
    abc = "New Global"
    print(abc)

changeGlobal()
print(abc)


