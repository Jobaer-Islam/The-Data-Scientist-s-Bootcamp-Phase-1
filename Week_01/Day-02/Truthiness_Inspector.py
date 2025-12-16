# Goal: Create an empty list
data = [] 

# The Truthiness Inspector in action:
# Since the list 'data' is empty ([]), it is Falsy.
if data:
    print("Data Found")
else:
    print("No Data") 
# Output: No Data 

# Example of a Truthy list:
data_found = [1, 2, 3]

if data_found:
    print("Data Found")
else:
    print("No Data") 
# Output: Data Found 
