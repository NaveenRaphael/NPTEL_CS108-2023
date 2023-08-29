# from random import random

# print("".join([el if random() < 0.7 else el.upper()
#       for el in input("Enter the text:").lower()]))


def factorial(n):
    print(".", end="")
    if n <= 1:
        return n
    return factorial(n-1)+factorial(n-2)


arr = [1, 2, 3, 5]


print(map(lambda w: w+3, arr))
