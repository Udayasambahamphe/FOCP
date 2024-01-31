#1
width = 104.32
height = 15.654
area = width * height
Area = f"The area of a rectangle with a width of {width} and a height of {height} is {area}."
print(Area)

#2
width = 104.32
height = 15.654
area = width * height
Area = f"The area of a rectangle with a width of {width} and a height of {height} is {area:.3f}."
print(Area)

#3
name= "Udaya"
age=19
print(f"{name:15} - {age:10}")

#4
name = "Udaya Limbu"
age = 19.890
print(f"{name:>20} {age:$>20.2f}")
    
#5
import math
r = 52
area = math.pi * r**2
area_of_circle = "Area of circle with a radius of {radius} is {area:.2f}.".format(radius=r, area=area)
print(area_of_circle)

#6
name = "Udayalimbu"
age = 19
string_formatting = "{name:@^15} {age:#^10}".format(name=name, age=age)
print(string_formatting)

#7
with open(r'C:\Users\ace\Desktop\info.txt', 'r') as file:
    for line in file:
        print(line,end='')

#8
with open(r'C:\Users\ace\Desktop\info.txt', 'r') as file:
    first_line = file.readline().strip()
    second_line = file.readline().strip()
    third_line = file.readline().strip()
    
print(first_line)
print(second_line)
print(third_line)

#9
with open(r'C:\Users\ace\Desktop\info.txt', 'r') as file:
    for line in file:
        print(line.strip())

#10

#11

#12
# f-strings: String formatting feature in Python, introduced in 3.6, allowing expressions inside curly braces within strings.
# Format Specifier: Controls the formatting of values within strings, specified after a colon inside curly braces in an f-string.
# File Modes: Indicate the operations that can be performed on a file, such as read ('r'), write ('w'), or append ('a').
# Binary Files: Handling non-text data in files by opening them in binary mode ('b'), commonly used for images or executables.
# Random Access: Refers to the ability to access data at any position in a file, facilitated by methods like seek().
# Exceptions: Events that disrupt the normal flow of a program, handled using try, except, else, and finally blocks for error management.