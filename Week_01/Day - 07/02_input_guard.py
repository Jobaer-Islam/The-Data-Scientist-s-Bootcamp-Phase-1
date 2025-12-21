"""
Concept: Input Guard
Prevents program crash due to invalid user input.
"""

while True:
    try:
        age = int(input("Enter your age: "))
        print("Your age is:", age)
        break
    except ValueError:
        print("Numbers only. Please try again.")
