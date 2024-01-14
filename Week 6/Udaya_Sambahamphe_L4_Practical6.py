#1
import math

squares = [1, 4, 9, 16, 25]
for square in squares:
    root = math.sqrt(square)
    print(root)

#2
squares = [1, 4, 9, 16, 25]
squares.append(49)
squares.append(64)
squares.append(81)
print(squares)

#3
squares.extend([121, 144, 169])
print(squares)

#4
squares.insert(0, 2)
print(squares)

#5
squares = [1, 4, 9, 16, 25,44,49]
squares.remove(49)
print(squares)

#6
squares = [1, 4, 9, 16, 25]
squares.remove(3)
print(squares)

#7
squares = [1, 2, 3, 1, 2]
squares.remove(2)
print(squares)

#8
squares = [1, 4, 9, 16, 25]

last_value = squares[-1]
print("Last value of the list: ", last_value)
squares.remove(last_value)
print("The updated list is:", squares)

#9
squares = [1, 4, 9, 16, 25]
first_value = squares.pop(0)
print("The first value of the list is:", first_value)
print("The updated list is:", squares)

#10
names = ['jim','Alice','Bob','Charlie','Eve']
names.sort()
print("The sorted list is:", names)

#11
names = [ "Eric", "anna", "Sophie", "sam"]
names.sort(key=lambda x: x.upper())
print("The sorted list is:", names)

#12
squares = [1, 4, 9, 16, 25]
squares.reverse()
print("The reversed list is:", squares)

#13
colours = ["red", "green", "yellow", "blue", "red"]
print(colours.index("blue"))

#14
colours = ["red", "green", "yellow", "blue", "red"]
colours_copy = colours.copy()

print("Original list: ", colours)
colours[0] = "black"
colours[1] = "white"

print("Modified original list: ", colours)
print("Copy: ", colours_copy)

#15
cubes = [x ** 3 for x in range(2, 21)]
print("Cubes of numbers:")

#16.The some_users list comprehension will contain the user names from 
# the all_users list where the length of the user name is less than 8.
# The condition that has to be met for inclusion is the length of the
# user name. Only those user names with a length less than 8 will be
# added to the some_users list.

#17
address = ("1819", "Bajrabarahi,Lalitpur", "H123")
print(address)

#18
address = ("1819", "Bajrabarahi,Lalitpur", "H123")
print(type(address))

#19
address = ("1819", "Bajrabarahi,Lalitpur", "H123")
ghar_no, ward_no, postcode = address
print(address)
print(type(ghar_no))

#20 
address = ("1819", "Bajrabarahi,Lalitpur", "H123")
print(*address)

#21
# Method: Function associated with objects in OOP.
# List Comprehension:cConcise list creation in Python.
# Tuple:cImmutable, ordered collection in parentheses.
# Tuple Packing:cImplicitly creating a tuple from values.
# Sequence Unpacking: Extracting values from a sequence into variables.