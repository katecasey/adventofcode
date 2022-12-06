instr = {}
rock = 1
paper = 2
scissors = 3
win = 6
draw = 3
lose = 0
totalScore = 0

# list of lists to hold the rules - their move, my move, my outcome (added later), my score (added later)
ruleBook = []
ruleBook.append(['A', 'X'])
ruleBook.append(['A', 'Y'])
ruleBook.append(['A', 'Z'])
ruleBook.append(['B', 'X'])
ruleBook.append(['B', 'Y'])
ruleBook.append(['B', 'Z'])
ruleBook.append(['C', 'X'])
ruleBook.append(['C', 'Y'])
ruleBook.append(['C', 'Z'])


def getOutcome(theirMove, myMove):
    outcome = lose
        #their rock loses to my paper
    if theirMove == 'A' and myMove == 'Y':
        outcome = win
        #their paper loses to my scissors
    if theirMove == 'B' and myMove == 'Z':
        outcome = win
        #their scissors loses to my rock
    if theirMove == 'C' and myMove == 'X':
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


def getScore(outcome, myMove):
    if myMove == 'X': 
        myMoveNum = rock
    if myMove == 'Y': 
        myMoveNum = paper
    if myMove == 'Z': 
        myMoveNum = scissors    
    
    return outcome + myMoveNum 


#Calculate the outcomes and scores and populate the rulebook
for move in ruleBook:
    outcome = getOutcome(move[0], move[1])
    move.append(outcome)
    move.append(getScore(outcome, move[1]))


#read in the file values and determine the result
with open('day2_input.txt', 'r') as file:
    play = 1
    score = 0
    outcomeConv = 0
    for line in file:
        key = 'play' + str(play)
        cleanLine = line.replace('\n', '')
        theirMove, outcome = cleanLine.split(' ')
        instr[key] = []
        instr[key].append(theirMove)        
        instr[key].append("")
        if outcome == 'X':
            outcomeConv = lose
        if outcome == 'Y':
            outcomeConv = draw
        if outcome == 'Z':
            outcomeConv = win
        instr[key].append(outcomeConv)
        #iterate through rule book to find my required move for the given outcome, populate the record
        for rule in ruleBook:
            if rule[0] == theirMove and rule[2] == outcomeConv:
                instr[key][1] = rule[1] #append the matching myMove
                instr[key].append(rule[3]) #append the matching score
        play += 1


for game in instr.keys():    
    totalScore += instr[game][3]


print('Total is: ' + str(totalScore))
