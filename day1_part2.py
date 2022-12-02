calories = {}
ind = 0
index = 'elf' + str(ind)
calories[index] = []
allTotals = []

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
    allTotals.append(total)

sortedTotals = sorted(allTotals, reverse=True)

print('Highest 3 calorie values are ' + str(sortedTotals[0]) + ', ' +  str(sortedTotals[1]) + ', ' + str(sortedTotals[2]) + '.')
print('The total of the highest 3 values is: ' + str(sortedTotals[0] + sortedTotals[1] + sortedTotals[2]) + '.')
