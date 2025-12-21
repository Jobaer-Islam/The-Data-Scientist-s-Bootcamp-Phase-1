"""
Concept: Math Safety Net
Handles division by zero safely.
"""

try:
    x = int(input("Enter a number: "))
    print(100 / x)
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Invalid input.")
