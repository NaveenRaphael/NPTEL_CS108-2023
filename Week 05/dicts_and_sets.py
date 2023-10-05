# Today's class
# - A lot more about dictionaries: what is a valid key?
# - A simpler version of a dictionary: A set
# - Interactive python notebooks

a = {}

a["First value"] = 1000
a[3] = 26622
a[1] = 1000

a[True] = 3000

a[23] = [1, 2, 3, 4]


b = {
    2: 34,
    5: 1,
    23: 100
}

c = {}

for key in a:
    c[key] = a[key]

for key in b:
    if key in c:
        c[key] = (a[key], b[key])
    else:
        c[key] = b[key]


print(a)
print(b)

print(c)


# Like for example, in your folder, have a file called lists.py
# which is full of things like:

a = [1, 2, 6, 4]
# -> Defining a list and putting values inside

for el in a:
    print(el)
    # Printing values in list

# and so on
# I had made this for another language i studied, called rust
