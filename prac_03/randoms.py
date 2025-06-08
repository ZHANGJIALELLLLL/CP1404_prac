import random

print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3
"""
What did you see on line 1?
Generate numbers between 5 and 20.
What was the smallest number you could have seen, what was the largest?
The smallest number is 5, the largest number is 20.

What did you see on line 2?
Start from the number 3 and stop at the number 10, generating two numbers at intervals.
What was the smallest number you could have seen, what was the largest?
The smallest number is 3, the largest number is 9.
Could line 2 have produced a 4?
NO

What did you see on line 3?
Generate numbers between 2.5 and 5.5.
What was the smallest number you could have seen, what was the largest?
The smallest number is 2.5, the largest number is 5.5.
"""
# Write code, not a comment, to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)
