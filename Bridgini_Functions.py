import random


def rotateList(list_in, x):
    # rotating the list to the left by 'x' steps
    return list_in[-x % len(list_in):] + list_in[:-x % len(list_in)]


def dealingCards_4p():
    # dealing the cards for 4 players
    deck = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
            "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
            "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]
    p1cards = []
    p2cards = []
    p3cards = []
    p4cards = []
    while len(p1cards) < 10:
        card = random.choice(deck)
        deck.remove(card)
        p1cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p2cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p3cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p4cards.append(card)
    return p1cards, p2cards, p3cards, p4cards


def dealingCards_3p():
    # dealing the cards for 3 players
    deck = ["r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
            "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
            "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
            "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]
    p1cards = []
    p2cards = []
    p3cards = []
    while len(p1cards) < 10:
        card = random.choice(deck)
        deck.remove(card)
        p1cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p2cards.append(card)
        card = random.choice(deck)
        deck.remove(card)
        p3cards.append(card)
    return p1cards, p2cards, p3cards


def leadingColor(card):
    # the color of the first card in each turn
    color = ''
    if card[0] == "r":
        color = "Red"
    elif card[0] == "b":
        color = "Blue"
    elif card[0] == "o":
        color = "Orange"
    elif card[0] == "g":
        color = "Green"
    return color


def isColorInList(cards, color):
    # check if a list of cards contains a specific color
    inList = False
    count = 0
    for i in range(len(cards)):
        if cards[i][0] == color:
            count += 1
    if count != 0:
        inList = True
    return inList


def isValidColor(card, color, isInList):
    # check if a chosen card has a valid color
    # input: a specific card (ex. 'g6'), a specific color (ex. 'g'), boolean if a specific card is in th players hand
    # output: True / False if a card is valid for play
    if card[0] == color:
        if isInList:
            return True
        else:
            return False
    else:
        return False


def isCardInList(cards, card):
    # check if a list of cards contains a specific card
    inList = False
    count = 0
    for i in range(len(cards)):
        if cards[i] == card:
            count += 1
    if count != 0:
        inList = True
    return inList


def getCardScore(card):
    # input the cards in turn and current score and updates the current score
    scoreDict = {"r1": 1, "r2": 1, "r3": 1, "r4": 1, "r5": 1, "r6": 1, "r7": 1, "r8": 1, "r9": 5, "r10": 1,
                 "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "b9": 3, "b10": 0,
                 "o1": 0, "o2": 0, "o3": 0, "o4": 0, "o5": 0, "o6": 0, "o7": 0, "o8": 0, "o9": 3, "o10": 0,
                 "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "g9": 3, "g10": 0}
    score = scoreDict[card]
    return score


def findMaxCard(turn):
    # finding the max card in a turn to check who takes all
    leadColor = turn[0][0]
    maxList = []
    for i in range(len(turn)):
        if turn[i][0] == leadColor:
            maxList.append(int(turn[i][1:]))
    maxNumber = max(maxList)
    maxCard = leadColor + str(maxNumber)
    return maxCard


def findPlayerWithMaxCard(turn, maxCard):
    # find the player name with the highest card per turn
    for i in range(len(turn)):
        if turn[i] == maxCard:
            return i


def getTurnScore(turn):
    # find the total score per turn (sum of 4 cards)
    turnScore = 0
    for i in range(len(turn)):
        turnScore += getCardScore(turn[i])
    return turnScore


def getLooserName(score, names):
    # returns the player with the most amount of bad points (if a tie will select randomly)
    # the looser will start the next round
    maxScore = max(score)
    looser = []
    for i in range(len(score)):
        if score[i] == maxScore:
            looser.append(names[i])
    if len(looser) == 1:
        return looser[0]
    else:
        index = random.randint(0, len(looser)-1)
        return looser[index]


def getWinnerName(score, names):
    # returns the winner score with the least amount of bad score (if a tie will display both)
    minScore = min(score)
    winner = []
    for i in range(len(score)):
        if score[i] == minScore:
            winner.append(names[i])
    if len(winner) == 1:
        return winner[0]
    else:
        print('There is a tie! there are multiple winners !')
        return winner
