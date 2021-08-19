import random


def rotateList(list_in, x):
    return list_in[-x % len(list_in):] + list_in[:-x % len(list_in)]


def dealingCards_4p(deck):
    p1cards = []
    p2cards = []
    p3cards = []
    p4cards = []
    while len(p1cards) < 10:  # dealing the cards for 4 players
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


def dealingCards_3p(deck):
    p1cards = []
    p2cards = []
    p3cards = []
    while len(p1cards) < 10:  # dealing the cards for 4 players
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


def leadingColor(card):  # the color of the first card in each turn
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


def isColorInList(cards, color):  # list of cards and color an check if color exist in list
    inList = False
    count = 0
    for i in range(len(cards)):
        if cards[i][0] == color:
            count += 1
    if count != 0:
        inList = True
    return inList


def isValidColor(card, color, isInList):
    if card[0] == color:
        if isInList:
            return False
        else:
            return True
    else:
        return True


def isCardInList(cards, card):
    inList = False
    count = 0
    for i in range(len(cards)):
        if cards[i][0] == card:
            count += 1
    if count != 0:
        inList = True
    return inList


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


def Bridgini(names):
    deck = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
            "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
            "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]

    player1Cards = []
    player2Cards = []
    player3Cards = []
    player4Cards = []
    playersScore = [0, 0, 0, 0]

    firstPlayer = random.choice(names)
    whoLost = ''
    roundNumber = 1

    if len(names) != 3 and len(names) != 4:  # checking for legal player count
        print("can't play, my Bridgini is designed for 3 or 4 players, try again")
        return

    # the first player decides what card to throw based on the name of the card (exact match)
    if roundNumber == 1:  # first round of the new game
        print('The first player (randomly chosen) is:', firstPlayer)
        rotate = names.index(firstPlayer)
        newNames = rotateList(names, -rotate)  # the correct playing order when first player is known
    else:
        print('The first player (lost the previous round) is:', whoLost)
        rotate = names.index(whoLost)
        newNames = rotateList(names, -rotate)  # the correct playing order when first player is known

    if len(names) == 4:
        player1Cards, player2Cards, player3Cards, player4Cards = dealingCards_4p(deck)

        while len(player1Cards) != 0:  # the actual game for 4 players

            print("cards for", newNames[0], ':', player1Cards)
            print("cards for", newNames[1], ':', player2Cards)
            print("cards for", newNames[2], ':', player3Cards)
            print("cards for", newNames[3], ':', player4Cards)

            print(newNames[0], ', Your turn to play')
            card1 = input('choose a card to throw:')
            player1Cards.remove(card1)
            print("Leading Color Is:", leadingColor(card1))

            print(newNames[1], ', Your turn to play')
            card2 = input('choose a card to throw:')
            while isValidColor(card2, card1[0], isColorInList(player2Cards, card1[0])) \
                    and not isCardInList(player2Cards, card2):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card2 = input('choose a card to throw:')
            player2Cards.remove(card2)

            print(newNames[2], ', Your turn to play')
            card3 = input('choose a card to throw:')
            while isValidColor(card3, card1[0], isColorInList(player3Cards, card1[0])) \
                    and not isCardInList(player3Cards, card3):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card3 = input('choose a card to throw:')
            player3Cards.remove(card3)

            print(newNames[0], ', Your turn to play')
            card4 = input('choose a card to throw:')
            while isValidColor(card4, card1[0], isColorInList(player4Cards, card1[0])) \
                    and not isCardInList(player4Cards, card4):
                print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                card4 = input('choose a card to throw:')
            player4Cards.remove(card4)

            turn = [card1, card2, card3, card4]
            print(newNames[0], ':', card1, ', \n', newNames[1], ':', card2, ',\n',
                  newNames[2], ':', card3, ',\n', newNames[3], ':', card4)

            maxCard = findMaxCard(turn)
            index = findPlayerWithMaxCard(turn, maxCard)
            turnScore = getTurnScore(turn)

            playersScore[index] += turnScore

            print("this turn score is:", playersScore)

# *** REQUIRED FIX ***
# if the player does not have the leading color he cant throw any color
# when round is lost assign 'whoLost' variable to the looser


p = ['Dor', 'Liran', 'Yoni', 'Ido']
Bridgini(p)
