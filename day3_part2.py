import string

mapping = []
priorityTotal = 0
common = ''
letterValue = 0

lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
letters = lower + upper
numbers = list(range(1,53))


for index in range (0, len(numbers)):
    mapping.append([numbers[index], letters[index]])


with open('day3_input.txt', 'r') as file:
    rucksacks = []
    for line in file:
        cleanLine = line.replace('\n', '')
        rucksacks.append(cleanLine)


for startLine in range(0, len(rucksacks), 3):
    for item in rucksacks[startLine]:
        if ((rucksacks[startLine + 1].find(item) != -1) and (rucksacks[startLine + 2].find(item) != -1)):
            common = item
    
    for pair in mapping:
        if common == pair[1]:
            letterValue = pair[0]      
    
    priorityTotal += letterValue
    
    #print('startLine: ' + str(startLine) + ', ' + 'rucksacks[' + str(startLine) + ']: ' + rucksacks[startLine] + ', ' + 'rucksacks[' + str(startLine + 1) + ']: ' + rucksacks[startLine + 1] + ', ' + 'rucksacs[' + str(startLine + 2) + ']: ' + rucksacks[startLine + 2] + ', common: ' + common + ', letterValue: ' + str(letterValue) + ', priorityTotal: ' + str(priorityTotal))
    common = ''
    letterValue = 0

print('Priority total is: ' + str(priorityTotal))
