#!/usr/bin/python3
#LISTS
a = [10, 20, 30, 40] # list of four integers
b = ["spam", "bungee", "swallow"] # list of three strings
c = ["hello", 2.0, 5, [10, 20]] # nested list
d = [] # empty list
if []: # Check if empty string
    print("This is true.")
else:
    print("This is false.") # The empty string is false in a boolean expression

# ASSIGNING LIST VALUES TO VARIABLES
vocabulary = ["ameliorate", "castigate", "defenestrate"]
numbers = [17, 123]
empty = []

# PASSING LISTS AS PARAMETERS
print(vocabulary, numbers, empty) 

# ACCESING ELEMENTS OF A LIST
# TypeError: list indices must be integers
# IndexError: list index out of range
print(numbers[0]) # Print the first element
print(numbers[9-8]) # Print the second element
print(numbers[-1]) # Print the last element
print(numbers[-2]) # Print the second to last element

# LIST TRANSVERSAL 
horsemen = ["war", "famine", "pestilence", "death"]

i = 0
# THE LENGTH OF A LIST : NUMBER OF ELEMENTS
num = len(horsemen)
while i < num:
    print(horsemen[i])
    i+=1
nest = ['spam!', 1, ['Brie', 'Roduefort', 'Pol le Veq'], [1, 2, 3]]
print(len(nest))

# LIST MEMBERSHIP
val = 'pestilence' in horsemen
print(val)
val = 'debauchery' in horsemen
print(val)
val = 'debauchery' not in horsemen
print(val)

# LIST OPERATIONS
e = [1, 2, 3] 
f = [4, 5, 6]

# +
g = e + f
print(g)

# *
h = [0]
print(h * 4)
print(e * 3)

# LIST SLICES
a_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(a_list[1:3])
print(a_list[1:1])
print(a_list[:4])
print(a_list[3:])
print(a_list[:])

# FUNCTION range()
print(list(range(1, 5)))
print(list(range(10)))
print(list(range(1, 10, 2)))
print(list(range(20, 4, -5)))
print(list(range(10, 10, -5)))

# LISTS ARE MUTABLE
fruit = ['banana', 'apple', 'quince']
fruit[0] = 'pear'
fruit[-1] = 'orange'
print(fruit)
# Item assignment
my_list = ['T', 'E', 'S', 'T']
my_list[2] = 'X'
print(my_list)
# update several elements at once
a_list[1:3] = ['x', 'y']
print(a_list)
# remove elements from a list by assigning the empty list to them
a_list[1:3] = []
print(a_list)
# add elements to a list by squeezing them into an empty slice 
a_list = ['a', 'd', 'f']
a_list[1:1] = ['b', 'c']
print(a_list)

a_list[4:4] = ['e']
print(a_list)



# LIST DELETION
a = ['one', 'two', 'three']
del a[1]
print(a)


del a_list[1:5]
print(a_list)
