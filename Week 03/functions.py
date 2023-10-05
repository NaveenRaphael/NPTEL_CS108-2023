q_no = 1


def print_question_no():
    global q_no
    print(f"Question {q_no}")
    q_no += 1


a = [2, 5, 8, 10, 5]
b = []
# Finding x^2 + 4x + 4
temporary = a[0]*a[0]
temporary = temporary + 4*a[0]
temporary = temporary + 4
b.append(temporary)


def my_quadratic(x):
    return x*x + 4*x + 4


# What is the output?
print_question_no()

print(my_quadratic(my_quadratic(-2)))

# ----
print_question_no()

a = 2


def p(a):
    print(a)
    a = 4
    print(a)
    return a


print(f"{p(a)}, {a}")

# ---
print_question_no()
