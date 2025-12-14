# Standard Input (Unsafe)
# age = input("Age: ") <-- Returns "25" (String)

# The Academy Standard (Safe)
raw_val = input("Enter Principal: ")
try:
    principal = float(raw_val) # Explicit Casting
    print(f"Accepted: ${principal:,.2f}") # F-String Formatting
except ValueError:
    print("Error: Invalid Number")
