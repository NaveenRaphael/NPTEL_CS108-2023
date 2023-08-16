q_no = 1


def print_question_no():
    global q_no
    print(f"---\nQuestion {q_no}")
    q_no += 1


print_question_no()

marks_of_students = [
    17,
    18,
    20,
    20
]

name_of_students = (
    "Naveen",
    "Diksha",
    "Kamal",
    "Manish")

name_of_students[0] = "Navin"

marks_of_students[1] = 20

print(marks_of_students[1])


# What is the output?
print_question_no()

a = (4, 6, 10, -2)
print(a[0])

print(a[-1])

print_question_no()

# a[1] = 4

print(a[1])

print_question_no()

b = [1, 4, 6, 8, 10]

b[1] = 5
print(b)


print_question_no()
# For loops
print("Showing for loops:")
for item in a:
    print(item*item)
print("---")

print("Showing for loops:")
for i in range(len(a)):
    print(a[i]*a[i])
print("---")


# Check if element is inside with in
b = [1, 4, 6, 8, 10, 12]


# Check is 5 is inside this list;
# I print "I found the number 5"

is_5_not_in_the_list_yet = True

for element in b:
    #print(f"The number i am checking is {element} \nChecking if its 5...")
    if element == 5:
        is_5_not_in_the_list_yet = False
        print("I found the number 5")
        break


if is_5_not_in_the_list_yet:
    print("I did not find the number")


print_question_no()
print(2+3 in [2, 3, 7, 4])
print(2+3 in (2, 3, 7, 5))
print(4 in range(10))
