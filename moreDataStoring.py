# A set cannot contain duplicate elements, even then if you store duplicates
# then at runtime they does not gets displayed
mySet = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5}
print(mySet)

# sets are unchangeable but you can add or remove items
# Also, since set items are unordered, tou cannot access the set items using keys or indices
# And when you display set items they being unordered gets displayed in multiple random ways
s1 = {"Apple", "Mango", "Banana", "Papaya"}
s1.add("Pineapple")
# we can delete items from sets using two methods, remove(), and discard
# if item to be deleted is not present in the given set, remove() method will raise an error
# while discard() method will not
s1.remove("Mango")
s1.discard("Mango")
print(s1)

# Adding elements to sets from other iterables
# You can add any iterables to sets, and not just sets
# we can use update() method or union() method
s2 = {"Mumbai", "Bengaluru", "Delhi"}
s3 = {"India", "USA", "Canada", "Australia", "UK", "Brazil"}
list1 = [1, 2, 3, 4, 5]

s2.update(s3)
s3.update(list1)
newSet = s2.union(list1)
print(s2)
print(s3)
print(newSet)

# clear or remove entire content of a set
s3.clear()
print(s3)

# This deletes the entire data structure
# del s3
# print(s3)

# Now, if you want to keep only the duplicates in the set or remove only duplicates,
# then we have multiple, methods for that

# 1. Keep only duplicates: intersection_update() or intersection()
mySet1 = {1, 2, 3, 4, 5}
mySet2 = {3, 4, 5, 6, 7}

mySet1.intersection_update(mySet2)  # or newSet = mySet1.intersection(mySet2)
print(mySet1)

# 1. Remove only duplicates: intersection_update() or intersection()
mySet3 = {1, 2, 3, 4, 5}
mySet4 = {3, 4, 5, 6, 7}

mySet3.symmetric_difference_update(mySet4)  # or newSet = mySet3.symmetric_difference(mySet2)
print(mySet3)

# Dictionaries
# Dictionaries can hold multiple data types together and also along with lists
myDict = {
    "brand": "Toyota",
    "Year": 1985,
    "Model": "Fortuner",
    "colours": ["black", "white", "grey"]
}

print(myDict)  # We can access items in dictionaries using keys

# to get keys and values from the dictionary we use following methods:
# You cannot access items from dictionaries using indices, as they're stored as key-value pairs
print(myDict.keys())  # 1. To get keys: keys()
print(myDict.values())  # 2. To get values of keys: values()

# a key value pair together is called an item in dictionary
print(myDict.items())  # This will print all the keys with their values in the tuple form

# check if the key exists in the dictionary

if "brand" in myDict:
    print("Yes \"brand\" is present in the dictionary")

# change values of keys in dictionary:
# we can use either method according to our convenience
myDict.update({"brand": "BMW"})   # Changes brand from Toyota to BMW
myDict["brand"] = "Toyota"    # Changing brand again
print(myDict)

# Looping through dictionary
# This will print all the keys in the dictionary
for x in myDict:
    print(myDict)

for x in myDict.keys():
    print(myDict)

# This will print all the key values in the dictionaries
for x in myDict:
    print(myDict[x])

for x in myDict.values():
    print(myDict)

# Printing the keys and values together
for x, y in myDict.items():
    print(x, y)

# Copying a dictionary
dict1 = myDict.copy()
print(dict1)

dict2 = dict(myDict)
print(dict2)


# Ways of creating nested dictionaries
# 1.
myFamily = {
    "child1" : {
        "Name": "Snehil",
        "Age": 21
    },
    "child2" : {
        "Name": "Pari",
        "Age": 13
    },
    "child3" : {
        "Name": "Manish",
        "Age": 27
    },

    "child4" : {
        "Name": "Shreya",
        "Age": 23
    }
}

print(myFamily)

# 2.
child1 = {
    "Name": "Snehil",
    "Age": 21
    }

child2 = {
    "Name": "Pari",
    "Age": 13
    }

child3 = {
    "Name": "Manish",
    "Age": 27
    }

child4 = {
    "Name": "Shreya",
    "Age": 23
    }

myFamily1 = {
    "child1": child1,
    "child2": child2,
    "child3": child3,
    "child4": child4
}

print(myFamily1)
