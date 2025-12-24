"""
O(N²) String Builder
Strings are immutable.
"""

s = ""
for _ in range(10_000):
    s += "a"

print(len(s))

#Correct way:

chars = []
for _ in range(10_000):
    chars.append("a")

s = "".join(chars)
