# List can store multiple types of data together in a single package(list)
list8 = [1, 2, 3, 4, 5]
list1 = ["apple", "mango", "banana"]
boolList = [True, False, True, True, False]
listMix = ["mango", 3, 5, 7, "banana", 10, "Delhi", "mango"]  # list also allows duplicates

print(list8)
print(list1)
print(boolList)
print(listMix)
print(type(listMix))  # In python lists are the objects of the class called lists

# Changing a range of data (5 is not included, so elements from 1 to 4 are only changed)
listMix[1:5] = ["English", "Hindi", "Maths", "Science"]
print(listMix)

# If you try inserting more items than you specified,
# it gets inserted at the place where you specified
list1[1:2] = ["cherry", "black current"]
print(list1)

# inserting new element using insert method
myList = ["a", "b", "c", "d", "e", "a"]
myList.insert(6, "b")
print(myList)

# We can extend any list my using extend() method, we can add any iterable to a list
# not necessarily a list only
l1 = [2, 3, 4, 5, 6]
l2 = ["a", "b", "c", "d", "e"]
tuple = (1, 2, 3, 4, 5)

l1.extend(l2)
l2.extend(tuple)  # We extended a tuple in the list
print(l1)
print(l2)

# list.clear()
# del list1       ->    This deletes list1 from the memory
print(list8)
print(list1)

# looping through a list
listLoop = ["One", "Two", "Three", "Four"]
for i in range(len(listLoop)):  # Loop through the entire list
    print(listLoop[i])

# Using list comprehension for appending list as per our conditions to a new list
# list comprehension just reduces the code in a way more efficient manner
newList = [x for x in list1 if "a" in x]
print(newList)

listLoop.sort(reverse=True)
print(listLoop)

# Copying lists
thisList = ["a", "b", "c", "d"]
ll = thisList.copy()
print(thisList)
print(ll)

# Methods to join lists, extend, +, or append method
LIST = ["a", "b", "c", "d"]
LIST2 = [1, 2, 3, 4, 5]

for i in LIST2:
    LIST.append(i)     # append() method adds only a single element at a single time

LIST.extend(LIST2)     # extend() function can add the entire list at once to another list
print(LIST)

# Since tuples are unchangeable, to add, replace ro remove elements from tuple
# you first need to convert it to a list
tuple1 = ("a", "b", "c", "d")
x = list(tuple1)
x[0] = "z"
print(x)

# Adding tuples to tuples (we're somehow allowed to do so in python)
tup1 = (1, 2, 3, 4)
tup2 = (5,)

tup1 += tup2
print(tup1)

# Unpacking of tuple
tup3 = ("apple", "mango", "banana", "papaya")

(x, y, *z) = tup3    # Asterisk sign puts all the remaining tuple item to that variable as a list
print(x)
print(y)
print(z)

# Multiplying the contents of a tuple
myTuple = tup3*2    # simply multiply the tuple with the number of times you want to multiply
print(myTuple)


