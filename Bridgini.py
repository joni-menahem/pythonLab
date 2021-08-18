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


def Bridgini(names):
    # assumptions - player1 is always first, player2 second etc.
    # also, there is no strategy and cards are chosen randomly.

    scoreDict = {"r1": 1, "r2": 1, "r3": 1, "r4": 1, "r5": 1, "r6": 1, "r7": 1, "r8": 1, "r9": 5, "r10": 1,
             "b1": 0, "b2": 0, "b3": 0, "b4": 0, "b5": 0, "b6": 0, "b7": 0, "b8": 0, "b9": 3, "b10": 0,
             "o1": 0, "o2": 0, "o3": 0, "o4": 0, "o5": 0, "o6": 0, "o7": 0, "o8": 0, "o9": 3, "o10": 0,
             "g1": 0, "g2": 0, "g3": 0, "g4": 0, "g5": 0, "g6": 0, "g7": 0, "g8": 0, "g9": 3, "g10": 0}

    deck = ["r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
            "b1", "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
            "o1", "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
            "g1", "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]

    deck3 = ["r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10",
             "b2", "b3", "b4", "b5", "b6", "b7", "b8", "b9", "b10",
             "o2", "o3", "o4", "o5", "o6", "o7", "o8", "o9", "o10",
             "g2", "g3", "g4", "g5", "g6", "g7", "g8", "g9", "g10"]

    player1Cards = []
    player2Cards = []
    player3Cards = []
    player4Cards = []
    player1Score = 0
    player2Score = 0
    player3Score = 0
    player4Score = 0

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

        print("cards for", newNames[0], ':', player1Cards)
        print("cards for", newNames[1], ':', player2Cards)
        print("cards for", newNames[2], ':', player3Cards)
        print("cards for", newNames[3], ':', player4Cards)

    if len(names) == 3:
        player1Cards, player2Cards, player3Cards = dealingCards_3p(deck3)

        print("cards for", newNames[0], ':', player1Cards)
        print("cards for", newNames[1], ':', player2Cards)
        print("cards for", newNames[2], ':', player3Cards)

    while len(player1Cards) != 0:  # the actual game for 4 players
        print(newNames[0], ', Your turn to play')
        card1 = input('choose a card to throw:')
        player1Cards.remove(card1)
        c = card1[0]  # the color of the first card in each turn
        leadingColor = ''
        turn = [card1]
        if c == "r":
            leadingColor = "Red"
        elif c == "b":
            leadingColor = "Blue"
        elif c == "o":
            leadingColor = "Orange"
        elif c == "g":
            leadingColor = "Green"
        print("Leading Color Is:", leadingColor)
        print(newNames[1], ', Your turn to play')
        card2 = input('choose a card to throw:')
        player2Cards.remove(card2)
        print(newNames[2], ', Your turn to play')
        card3 = input('choose a card to throw:')
        player3Cards.remove(card3)
        print(newNames[0], ', Your turn to play')
        card4 = input('choose a card to throw:')
        player4Cards.remove(card4)

        print(newNames[0], ':', card1, ',', newNames[1], ':', card2, ',',
              newNames[2], ':', card3, ',', newNames[3], ':', card4)

# need to validate input when trowing a card if it exist on list
# need to check for if leading color exist and block any other card
# when round is lost assign 'whoLost' variable to the looser


x = ['Dor', 'Liran', 'Yoni', 'Ido']
Bridgini(x)
