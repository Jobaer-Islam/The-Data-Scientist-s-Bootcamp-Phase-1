# A classic computer math quirk
result = 0.1 + 0.2 
print(f"The raw value: {result}") # 0.30000000000000004

# Using an f-string to show only 2 decimal places
print(f"The clean value: {result:.2f}") # 0.30


Why it works: The :.2f inside the curly braces is a "format specifier." 
It tells Python: "I know the raw number is messy, but only show the user a fixed-point float with 2 decimal places."
