phrase = "python is fun"

# This looks like it changes the string, but it actually creates a NEW one
phrase.upper() 
print(f"Original: {phrase}") # Still "python is fun"

# To keep the change, you must reassign the variable name to the new object
phrase = phrase.upper()
print(f"Updated: {phrase}")  # "PYTHON IS FUN"


Why it works: Strings are "immutable" (unchangeable). Methods like .upper() 
or .replace() never edit the original string; they always hand you back a brand-new string.
