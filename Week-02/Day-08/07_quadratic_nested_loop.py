"""
O(N²) Nested Loop
Comparing every element with every other.
"""

list_a = range(1000)
list_b = range(1000)

matches = []
for a in list_a:
    for b in list_b:
        if a == b:
            matches.append(a)

print(len(matches))
