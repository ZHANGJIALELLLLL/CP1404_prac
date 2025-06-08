"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur when the user inputs an integer value
2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the denominator input by the user is 0.
Yes, before performing division operations, first check if the denominator is zero.
If the denominator is zero, we prompt the user to enter a non-zero value.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print("Value cannot be zero, place enter a non-zero value.")
    else:
        fraction = numerator / denominator
        print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")