# Standard Input (Unsafe)
# age = input("Age: ") <-- Returns "25" (String)

# The Academy Standard (Safe)
raw_val = input("Enter Principal: ")
try:
    principal = float(raw_val) # Explicit Casting
    print(f"Accepted: ${principal:,.2f}") # F-String Formatting
except ValueError:
    print("Error: Invalid Number")


Why it works: The try block attempts the "dangerous" conversion. If the user types a word
instead of a number, the except block catches the error before it can crash your program.
