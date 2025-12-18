"""
Concept: Mutability and Reference Trap
Lists are mutable and assignments copy references, not data.
"""

a = [1, 2, 3]
b = a          # reference copy

b[0] = 99

print("a:", a)
print("b:", b)

print("\nFix using copy():")

a = [1, 2, 3]
b = a.copy()   # real copy

b[0] = 99

print("a:", a)
print("b:", b)
