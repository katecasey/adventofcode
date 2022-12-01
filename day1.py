calories = {}
index = 0
calories["elf" + str(index)] = []
highestCal = 0
highestElf = ''


with open('day1_input', 'r') as file:
    for line in file:
        if line.rstrip('\n') != '':
            calories["elf" + str(index)].append(line.rstrip('\n'))
        else:
            index += 1 
            calories["elf" + str(index)] = []


for elf in calories.keys():
    total = 0
    for item in calories[elf]:
        total += int(item)
    if total > highestCal:
        highestCal = total
        highestElf = elf

print('Highest calorie value is ' + str(highestCal) + ' from ' + highestElf + '.')
