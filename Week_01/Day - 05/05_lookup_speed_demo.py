"""
Concept: Lookup Speed Comparison
List search is O(N), Dict/Set search is O(1).
"""

# Simulated large data
numbers_list = list(range(100000))
numbers_set = set(numbers_list)
numbers_dict = {x: True for x in numbers_list}

print("Check -1 in list:", -1 in numbers_list)
print("Check -1 in set:", -1 in numbers_set)
print("Check -1 in dict:", -1 in numbers_dict)
