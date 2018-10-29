# Write a program to print all the combinations of factors of given number n.
# Given the input 16, your output should be as follows:
#  [[2, 2, 2, 2,], [2 2 4], [2 8], [4 4]]


def combo(total):
    
    total = factCombo(16)

print(total)


def factCombo(n):

    if n < 0:
        return None
    if n == 0:
        return n

    return factCombo(n % 2) 



    
    