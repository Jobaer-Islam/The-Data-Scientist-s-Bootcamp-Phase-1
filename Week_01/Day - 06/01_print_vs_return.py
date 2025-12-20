"""
Concept: Print vs Return

print() shows output on screen.
return sends data back to the caller.
"""

def add_print(a, b):
    print(a + b)

result = add_print(5, 5)
print("Result from print function:", result)


def add_return(a, b):
    return a + b

result = add_return(5, 5)
print("Result from return function:", result)
