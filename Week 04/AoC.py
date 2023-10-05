elves = []

with open('AoC_D1.txt', 'r') as f:
    calory_count = []
    for line in f.readlines():
        if line.strip() != "":
            calory_count.append(int(line.strip()))
        else:
            elves.append(calory_count)
            calory_count = []

# Finds the calories held by each elf
calory_of_each_elf = [sum(elf) for elf in elves]

print(max(calory_of_each_elf))
