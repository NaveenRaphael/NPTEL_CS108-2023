# Function and program to check the number of occurance of a word in a file

# Exercise for you; how would you change this to check the occurance of multiple words?

def words(check):
    count = 0  # The number of times the word has been encountered
    print(words)

    with open('generic_text.txt', 'r') as f:
        file = f.readlines()
        for line in file:
            # I want to split based on " ", "." and ","; So i will convert all the . and , to empty space and then split
            line = line.replace(".", " ").replace(",", " ") #I "chained" a method call, think about what has happened here
            word_split = line.split()
            # print(word_split)
            count += word_split.count(check)
    return count

print(words('Python'))
