left_hand = "Coffee"
right_hand = "Tea"

# Swap them in one line!
left_hand, right_hand = right_hand, left_hand

print(f"Left Hand: {left_hand}")   # Tea
print(f"Right Hand: {right_hand}") # Coffee

Why it works: Python creates a hidden "package" (a tuple) containing (right_hand, left_hand) first,
then opens that package and assigns the contents to the names on the left side.
