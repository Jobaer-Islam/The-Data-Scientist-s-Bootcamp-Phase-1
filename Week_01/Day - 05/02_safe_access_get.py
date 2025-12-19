"""
Concept: Safe Dictionary Access
Using .get() prevents KeyError if key is missing.
"""

user = {"id": 1}

# Unsafe access (will crash if uncommented)
# print(user["email"])

# Safe access
email = user.get("email")
print("Email:", email)

# Safe access with default value
email = user.get("email", "No Email Found")
print("Email with default:", email)
