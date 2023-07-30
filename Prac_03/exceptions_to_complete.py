"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        # TODO: this line
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
        # TODO - add the exception you want to catch after except
print("Valid result is:", result)
