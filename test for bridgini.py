def getCardScore(card):  # input the cards in turn and current score and updates the current score
    scoreDict = {"r1": 1, "r2": 1, "r3": 1, "r4": 1, "r5": 1, "r6": 1, "r7": 1, "r8": 1, "r9": 5, "r10": 1,
                 "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "b9": 3, "b10": 0,
                 "o1": 0, "o2": 0, "o3": 0, "o4": 0, "o5": 0, "o6": 0, "o7": 0, "o8": 0, "o9": 3, "o10": 0,
                 "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "g9": 3, "g10": 0}
    score = scoreDict[card]
    return score


def findMaxCard(turn):
    leadColor = turn[0][0]
    maxList = []
    for i in range(len(turn)):
        if turn[i][0] == leadColor:
            maxList.append(int(turn[i][1:]))
    maxNumber = max(maxList)
    maxCard = leadColor + str(maxNumber)
    return maxCard


def findPlayerWithMaxCard(turn, maxCard):
    for i in range(len(turn)):
        if turn[i] == maxCard:
            return i


def getTurnScore(turn):
    turnScore = 0
    for i in range(len(turn)):
        turnScore += getCardScore(turn[i])
    return turnScore


turn = ['o5', 'r10', 'g9', 'r9']

maxCard = findMaxCard(turn)
index = findPlayerWithMaxCard(turn, maxCard)
turnScore = getTurnScore(turn)
print(maxCard)
print(index)
print(turnScore)

