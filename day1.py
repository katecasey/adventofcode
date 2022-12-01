calories = {}

calories["elf1"]=[1000, 2000, 3000]
calories["elf2"]=[4000]
calories["elf3"]=[5000, 6000]
calories["elf4"]=[7000, 8000, 9000]
calories["elf5"]=[10000]

highestCal = 0
highestElf = ""

for elf in calories.keys():

    total = 0
    for item in calories[elf]:
        total += item
    if total > highestCal:
        highestCal = total
        highestElf = elf

print('Highest calorie value is ' + str(highestCal) + ' from ' + highestElf + '.')    
