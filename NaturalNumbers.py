# Define a function that returns the sum of natural numbers
# Given an input number 6,
# your function should output 21 which it gets 
# by computing 6 + 5 + 4 + 3 + 2 + 1.


def natural(n):

    if n < 0:
        return None
    elif n == 0:
        return n
    elif n == 1:
        return n
    else:
        return natural(n-1) + n

print(natural(10))