def append_one(l: list): #we define the parameter type for readability in Python it wont enforce
    l.append(1) # Append an integer (1) to the end of list l.
    
x = [] # This is an empty list.
print(f"before append: {x}") # Prints [0].
append_one(x)
print(f"after append: {x}") # Prints [1].
