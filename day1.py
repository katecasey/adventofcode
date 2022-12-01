calories = {}
ind = 0
index = 'elf' + str(ind)
calories[index] = []
highestCal = 0
highestElf = ''

with open('day1_input.txt', 'r') as file:
    for line in file:
        cleanLine = line.rstrip('\n')
        if cleanLine != '':
            calories[index].append(cleanLine)
        else:
            ind += 1 
            index = 'elf' + str(ind)
            calories[index] = []

for elf in calories.keys():
    total = 0
    for item in calories[elf]:
        total += int(item)
    if total > highestCal:
        highestCal = total
        highestElf = elf

print('Highest calorie value is ' + str(highestCal) + ' from ' + highestElf + '.')
