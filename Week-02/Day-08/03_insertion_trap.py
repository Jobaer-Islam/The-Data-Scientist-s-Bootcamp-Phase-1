"""
O(N) Insertion Trap
Inserting at index 0 shifts all elements.
"""

data = list(range(10_000))
data.insert(0, -1)

print("Inserted at start")
