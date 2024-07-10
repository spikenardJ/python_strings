# Question 2: User Input Data Processor

# Task 1:  Input Length Validator

while True:
    first_name = input("Please enter your first name: ")
    last_name = input("Please enter your last name: ")
    both_names = len(str(first_name)) + len(str(last_name))
    if len(str(first_name)) < 2:
        print("First name is too short, please try again with at least two letters.")
    if len(str(last_name)) < 2:
        print("Last name is too short, please try again with at least two letters.")
    if len(str(first_name)) >= 2 and len(str(last_name)) >= 2:
        print(f"Your first name is {len(str(first_name))} letters and, your last name is {len(str(last_name))} letters.")
        print(f"Both of your names are {str(both_names)} letters.")

 