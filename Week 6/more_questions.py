# ignore
import random
import string
q_no = 1


def print_question_no():
    global q_no
    print(f"Question {q_no}")
    q_no += 1


print_question_no()
# Write a function to calculate the factorial of a number


def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)
    # product = 1
    # for i in range(1, n+1):
    #     product = i * product
    # return product


print(factorial(5))


print_question_no()
# What is the output?


def f(x, y):
    if x <= 0:
        return y
    return f(x-1, y+1)


print(f(10, 20))


print_question_no()
# Can you write a function that calculates square root to
# a specified precision, without using the inbuilt square root function?


def my_sqrt(num, precision, guess=1):
    if abs(guess*guess - num) < precision:
        return guess

    temp = num/guess
    return my_sqrt(num, precision, (temp + guess)/2)


sqrt3 = my_sqrt(3, 0.00001)
print(
    f"the sqrt of 3 is : {sqrt3}, and when we square it we get {sqrt3*sqrt3}")


print_question_no()
# Can you make a recursive function that checks if a string is a palindrome?


def check_palindrome(s):
    if s == "":
        return True
    if len(s) == 1:
        return True

    if s[0] != s[-1]:
        return False
    return check_palindrome(s[1:-1])


print(check_palindrome("HHEHEHHH"))

print_question_no()
# What is the output of this code?


def ex(a, n):
    if n < 0:  # If n is negative; we take the expoenet of 1/a instead
        return ex(1/a, -n)
    if n == 0:
        return 1  # if n is 0; the expoenent is always 1
    if n == 1:
        return a  # if n is 1; we get a

    temp = ex(a, n//2)
    if n % 2 == 0:
        return temp*temp
    return temp*temp*a


print(ex(5, 3))

print_question_no()
# Make a function that returns a dictionary whose keys are numbers, and values is the factors of that number


def get_factor(n):
    return [i for i in range(1, n+1) if n % i == 0]


def generate_factors(n):
    return {i: get_factor(i) for i in range(1, n+1)}


print(generate_factors(10))
