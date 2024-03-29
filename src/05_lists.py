# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
x.append(4)
print("Add 4 to x list:", x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
x.extend(y)
print("Combine x and y lists:", x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
x.pop(4)
print("Remove 8 from x list:", x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
x.insert(5, 99)
print("Insert 99 into x list:", x)

# Print the length of list x
print("Length of x list", len(x))

# Print all the values in x multiplied by 1000
print("Multiplied values", [i*1000 for i in x])  # Comprehension

for i in x:
    print(f"{i} multiplied by 1000", i * 1000)
