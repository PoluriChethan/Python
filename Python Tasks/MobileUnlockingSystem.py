# Correct PIN set for unlocking mobile
correct_pin = 2149

# Maximum number of attempts allowed
attempts = 3

# Display message to user
print("Enter PIN to unlock mobile : ")

# Loop runs for given number of attempts (3 times)
for attempt in range(attempts):
    
    # Take PIN input from user
    # attempt + 1 is used because range starts from 0
    pin = int(input(f"Attempt {attempt + 1} : "))

    # Check if entered PIN is correct
    if pin == correct_pin:
        print("Mobile is unlocked successfully")
        break   # Exit loop if PIN is correct

    else:
        # Calculate remaining attempts
        remaining = attempts - attempt - 1
        
        # If attempts are still left
        if remaining > 0:
            print(f"Wrong PIN! {remaining} attempts left.")
        
        # If no attempts left
        else:
            print("All attempts failed. Mobile Locked!")

# Just prints an empty line at the end
print()
