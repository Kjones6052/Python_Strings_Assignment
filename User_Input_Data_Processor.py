# Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name. Both should be at least 2 characters long. 
# If not, print an error message.

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
full_name = first_name + last_name
if len(first_name) >= 2 and len(last_name) >= 2:
    print(f"Thank you {first_name} {last_name}")
else:
    print("There has been an error.")