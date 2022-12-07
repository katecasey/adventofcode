import string

mapping = []
priorityTotal = 0

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
        capacity = len(cleanLine)
        halfCapacity = int(capacity / 2)
        firstHalf = cleanLine[0:halfCapacity]
        secondHalf = cleanLine[halfCapacity:capacity]
        compartments = [firstHalf, secondHalf]
        common = ''
        for item in firstHalf:
            if secondHalf.find(item) != -1:
                common += item
        if len(common) > 1:
            common = common[0]
        compartments.append(common)
        letterValue = 0
        for pair in mapping:
            if common == pair[1]:
                letterValue = pair[0]    
        compartments.append(letterValue)
        rucksacks.append(compartments)


for bag in rucksacks:
    priorityTotal += bag[3]    


print('Priority total is: ' + str(priorityTotal))
