instr = {}
rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
lose = 0
totalScore = 0


def getOutcome(theirMove, myMove):
    outcome = lose
        #their scissors loses to my rock
    if theirMove == 'C' and myMove == 'X':
        outcome = win
        #their rock loses to my paper
    if theirMove == 'A' and myMove == 'Y':
        outcome = win
        #their paper loses to my scissors
    if theirMove == 'B' and myMove == 'Z':
        outcome = win
        #rock and rock draws
    if theirMove == 'A' and myMove == 'X':
        outcome = draw
        #paper and paper draws
    if theirMove == 'B' and myMove == 'Y':
        outcome = draw
        #scissors and scissors draws
    if theirMove == 'C' and myMove == 'Z':
        outcome = draw
    return outcome


with open('day2_input.txt', 'r') as file:
    move = 1
    score = 0
    for line in file:
        key = 'move' + str(move)
        cleanLine = line.replace('\n', '')
        theirMove, myMove = cleanLine.split(' ')
        instr[key] = []
        instr[key].append(theirMove)        
        instr[key].append(myMove)
        if myMove == 'X': 
            instr[key].append(rock)
        if myMove == 'Y': 
            instr[key].append(paper)
        if myMove == 'Z': 
            instr[key].append(scissors)
        score = instr[key][2] + getOutcome(instr[key][0], instr[key][1]) 
        instr[key].append(score)
        move += 1


for game in instr.keys():    
    totalScore += instr[game][3]


print('Total is: ' + str(totalScore))
