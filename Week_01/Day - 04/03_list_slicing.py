"""
Concept: List Slicing
Syntax: list[start : stop : step]
Creates a new list (shallow copy)
"""

data = [10, 20, 30, 40, 50]

subset = data[1:4]
reverse = data[::-1]
last_three_reversed = data[-1:-4:-1]

print("Original:", data)
print("Subset:", subset)
print("Reverse:", reverse)
print("Last 3 reversed:", last_three_reversed)
