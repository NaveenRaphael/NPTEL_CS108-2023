
a = 2
print(a**a)


a = 3
b = 2

a = b
b = a

print(a, b)

a = 6
a = a+5

print(a)


a = 9
b = a+b

print(a, b)


a = 12
b = 17
a = a+b
b = a-b
a = a-b
print(a, b)


a = "hello "
b = "there!"
c = a+b
print(c)


a = 10
if a > 5:
    print("a is bigger than 5!")
print("The end")


a = 12
if a > 12:
    print("a is bigger than 12!")
print("The end!")

a = 5
if a+1 == 6:
    print("the value of a is quite definitely 5")
else:
    print("I suppose a is not 5")
print("The end!")


age = 15
if 12 < age < 20:
    print("This is a teen!")
else:
    print("Not a teen!")

a = 10
for i in range(10):
    print(a)
print("Over")

a = 5
for i in range(a):
    print(i, a)
print("done")

a = 12
if (a % 2) == 0:
    print("a is divisible by 2")
else:
    print("a is not divisible by 2")
print("duh")

a = 5
for i in range(20):
    if (i % a) == 0:
        print(i, " divisible!")
print("done!")

a = 4
for i in range(2):
    for j in range(3):
        print(i, j, a)
