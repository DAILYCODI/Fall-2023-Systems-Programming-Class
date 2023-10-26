#!/usr/bin/env python3

def add_func(a, b):
    c = a + b
    return c


def sub_func(a, b):
    return a - b

add_result = add_func(5,4)
print(f"Add: {add_result}")

sub_result = sub_func(5, 4)
print(f"Sub: {sub_result}")


#a = 10
#b = 3
#c = a // b
#print(c)

# python is space senstive
#-------------- IF & ELIF ---------------------
#if c > 5:
#    print("greater")
#elif c < 5:
#    print("less")
#else:
#    print("equal")

# ---------------List----------------
#numbers = [1, 2, 3, 4] # list 

# a list can also be letters
#letters = ["a", "b", "c", "d"]

#for letter in letters:
#    print(letter)

#for number in numbers:
#    print(number)
#    new_number = number + 2
#    print(new_number)
   

#print("hello")
# divison in python2 is an integer
# divison in python3 is an float
# / divison as a float
# // floor divison
# % remanider

#---------------ways to check the type of data---------------
#print(type(10.0))

#print("hello", a)

#---------ways to create a formatted string---------------
#first
#f = format
#print(f"{a} plus {b} = {c}")

#second
#print(f"{3} + {4} = {7}".format(a, b, c))


#h = "hello "
#w = "world"

#comments out information
#c = a + b
#print (c)

#print("helo " + "world")
#print("hello" , a)