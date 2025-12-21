"""
Concept: finally Block
Runs no matter what – success or failure.
"""

try:
    num = int(input("Enter number: "))
    print(10 / num)
except ZeroDivisionError:
    print("Division by zero error.")
except ValueError:
    print("Invalid input.")
finally:
    print("Execution complete.")
