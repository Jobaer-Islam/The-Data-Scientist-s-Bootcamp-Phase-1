"""
Concept: Scope & Stack Frames
Variables inside functions are local by default.
"""

x = 10

def change_x():
    x = 20   # local variable
    print("Inside function x:", x)
  

change_x()
print("Outside function x:", x)
