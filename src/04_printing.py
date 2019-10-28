"""
Python provides a number of ways to perform printing. Research
how to print using the printf operator, the `format` string
method, and by using f-strings.
"""

x = 10
y = 2.24552
z = "I like turtles!"

# Using the printf operator (%), print the following feeding in the values of x,
# y, and z:

# %i - Signed integer, %f - Floating point decimal format, %s - converts any python object using str()
print("Formatted Output:", "x is %i, y is %f, z is %s" % (x, y, z))

# Use the 'format' string method to print the same thing
print("Format:", "x is {x}, y is {y}, z is {z}".format(x=x, y=y, z=z))

# Finally, print the same thing using an f-string
print("f-string:", f'x is {x}, y is {y}, z is {z}')
