# Short hand for if-else
a = 200
b = 200
print("b > a") if b > a else print("a > b")

# Multiple if-e;se statements in a single line
print("b > a") if b > a else print("a = b") if a == b else print("a > b")

# For some conditions where you want to skip the if condition but have to keep it then simply pass it:
# this avoids error
x = 20
y = 30

if x < y:
    pass

# In python we have 2 types of loops - for loop and while loop

i = 1
while i < 7:
    print(i)
    i += 1
