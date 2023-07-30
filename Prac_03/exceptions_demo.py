"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs in programming when a function or operation receives an argument with the correct data type, but the value of the argument is inappropriate or invalid for the operation being performed.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs in programming when you attempt to divide a number by zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Sure I fix the code below.And I use the while loop for error checking about Zerodevide
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Can not divide by zero!")
        denominator = int(input("Enter the denominator: "))

    fraction = numerator / denominator
    print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
