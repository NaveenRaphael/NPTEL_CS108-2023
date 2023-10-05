# Today's class
# recursion

# Class will begin at 6


def sum_till(n):
    if n <= 1:
        return n
    return n + sum_till(n-1)


# print(sum_till(5))


# # Newtons method

# num = 100
# guess = 1.5
# for _ in range(10):
#     # print(guess)
#     temp = num/guess
#     guess = (guess+temp)/2
# print(f"the square of guess is {guess*guess}")


# #About default parameters
# def my_print(s="You did not input a value"):
#     print(s)


# my_print("hello")
# my_print()


# You are given a string S. Write a function count_letters which will return a dictionary containing letters (including special character) in string S as keys and their count in string S as values.

# (input and output will be handled by us you just need to write the function and return the dictionary)

# Input
# The Joy of computing

# Output
# {'T': 1, 'h': 1, 'e': 1, ' ': 3, 'j': 1, 'o': 3, 'y': 1, 'f': 1, 'c': 1, 'm': 1, 'p': 1, 'u': 1, 't': 1, 'i': 1, 'n': 1, 'g': 1}

# Explanation: T is appeared once in the string, similarly o is appeared 3 times in the string and so on. (You do not have to worry about the order of arrangement in your dictionary)

# def count_letters(s):
#     dictionary = {}
#     for letter in s:
#         # print(
#         # f"the letter i am looking at right now is {letter};\nThe dictionary looks like {dictionary}")
#         if not (letter in dictionary):
#             dictionary[letter] = 1
#         else:
#             dictionary[letter] = dictionary[letter] + 1
#     return dictionary


# dictionary = {
#     "name": "Naveen",
#     "age": 25,
#     "DOB": "Hah you thought ill write my actual DOB here",
#     "Profession": "Eating food",
#     "FullName": "Naveen"
# }

# dictionary["A new key!"] = "A new value!"

# a = [2, 5, 7, 98, 4, 4]
# dictionary["DOB"]

# dictionary.pop("DOB")

# print(dictionary.keys())


# print(range(1, 2, 9).__repr__())
# # Human readable representation of the "class"


# You are given a list L. Write a function uniqueE which will return a list of unique elements is the list L in sorted order. (Unique element means it should appear in list L only once.)

# Input will be handled by us

# Input
# [1,2,3,3,4,4,2,5,6,7]

# Output
# [1,5,6,7]

# Explanation

# Elements 1,5,6,7 appears in the input list only once.

# def uniqueE(L):
#     dictionary = {}
#     for el in L:
#         # print(
#         # f"the letter i am looking at right now is {letter};\nThe dictionary looks like {dictionary}")
#         if not (el in dictionary):
#             dictionary[el] = True
#         else:
#             dictionary[el] = False

#     M = []
#     for key in dictionary:
#         if dictionary[key]:
#             M.append(key)
#     M.sort()
#     return M


# print(uniqueE([1, 2, 3, 3, 4, 4, 2, 5, 6, 7]))


# You are given a list L. Write a program to print first prime number encountered in the list L.(Treat numbers below and equal to 1 as non prime)

# Input will be handled by us.

# Input
# [1,2,3,4,5,6,7,8,9]

# output
# 2

# Explanation
# Since 2 is the first prime number is list L, therefor it is printed.
# L = [60911941]*10000

L = L = [60911941]*100000 + [1, 10, 10, 10, 10, 20, 3, 4, 5, 6, 7, 8, 9]

dictionary = {}


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


def my_is_prime(n):
    if n in dictionary:
        return dictionary[n]
    if n <= 1:
        dictionary[n] = False
        return False
    for i in range(2, n//2):
        if n % i == 0:
            dictionary[n] = False
            return False
    dictionary[n] = True
    return True

# Memoisation


for i in L:
    if my_is_prime(i):
        print(i, end='')
        break

a = [3, 6, 87, 0, 9, 4, 5, 6, ]

dictionary = {
    "name": "Naveen",
    "age": 25,
    "DOB": "Hah you thought ill write my actual DOB here",
    "Profession": "Eating food",
    "FullName": "Naveen"
}

a[0]

dictionary["name"]
