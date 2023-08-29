# Today's class:
# List comprehension, and its cousins
# recursive functions (to understand this, we need to understand recursive functions)
# A lot of practice questions


# def generic_math_function(a):
#     return a+4

# a = [2,4,7,8,11]


# b = [
#      generic_math_function(element)
#      for element in a if element%2 == 0
#      ]

# print(a)
# print(b)


# Write a program that given some text writes the text in "Sarcastic SpongeBob" form

# like convert "I do not know what the sarcastic spongebob meme is" to "i Do NoT knOw wHat ThE sarcastIC spoNgEbob Meme Is"

import string
from random import randint, gauss

# Ternery operator

# print([gauss(0, 1) for i in range(10)])


def random_change(letter):
    return (letter.upper() if gauss(0, 1) > 0 else letter.lower())


# text = input("Enter the text ")

# # for character in text:
# #     if random.random() < 0.8:
# #         print(character.upper(), end="")
# #     else:
# #         print(character.lower(), end="")

# print()

# for character in text:
#     print(random_change(character), end="")

# print()

# print("".join([random_change(character) for character in text]))


# string = "..."

# print(string.join(["Hello", "there", "why", "speech"]))

num = int(input("Tell me a number pls"))
# fibonacci_numbers = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368]


# previous_2 = 0
# previous_1 = 1

# if num == 1:
#     print(0)
# if num == 2:
#     print(1)

# index = 2
# next_fibo = 1
# while index <= num:
#     next_fibo = previous_1 + previous_2
#     previous_2 = previous_1
#     previous_1 = next_fibo
#     index = index + 1
# print(next_fibo)

# while index <= num:
#     index, previous, next_num = index+1, next_num,  previous + next_num
# print(next_num)


# def fibo(n):
#     if n <= 1:
#         return n
#     return fibo(n-1) + fibo(n-2)


# print([fibo(num) for num in range(25)])
def mySqrt(x: int) -> int:
    i = 0
    while i*i < x:
        i = i+1
    return i-1


print(mySqrt(8))
