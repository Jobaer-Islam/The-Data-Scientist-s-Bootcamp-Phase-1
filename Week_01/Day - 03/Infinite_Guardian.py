# The Infinite Input Pattern

while True:  # Starts a loop that will run forever unless stopped
    pwd = input("Set Password (min 5 chars): ")
    
    # Check if the password length is 5 or more
    if len(pwd) >= 5:
        print("Password Set")
        break  # <--- EMERGENCY BRAKE! The loop stops now.
    
    # This line runs only if the password was too short (less than 5 chars)
    print("Too short. Try again.") 
