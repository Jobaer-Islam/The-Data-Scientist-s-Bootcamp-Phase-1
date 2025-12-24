"""
O(N) Linear Scan
Search for an element in a list.
"""

data = list(range(10_000))
target = -5

found = False
for item in data:
    if item == target:
        found = True
        break

print("Found:", found)
