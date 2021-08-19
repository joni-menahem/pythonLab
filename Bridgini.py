import random
from Bridgini_Functions import *


def Bridgini(names):

    playersScore = [0, 0, 0, 0]
    whoLost = ''
    roundNumber = 4
    firstPlayer = random.choice(names)

    if len(names) != 4:  # checking for legal player count
        print("can't play, my Bridgini is designed for 4 players, try again")
        return

    while roundNumber != 0:
        # the first player decides what card to throw based on the name of the card (exact match)
        if roundNumber == 4:  # first round of the new game
            print('The first player (randomly chosen) is:', firstPlayer)
            rotate = names.index(firstPlayer)
            newNames = rotateList(names, -rotate)  # the correct playing order when first player is known
        else:
            print('The first player (lost the previous round) is:', whoLost)
            rotate = names.index(whoLost)
            newNames = rotateList(names, -rotate)  # the correct playing order when first player is known

        if len(names) == 4:
            player1Cards, player2Cards, player3Cards, player4Cards = dealingCards_4p()

            while len(player1Cards) != 0:  # the actual game for 4 players

                print("cards for", newNames[0], ':', player1Cards)
                print("cards for", newNames[1], ':', player2Cards)
                print("cards for", newNames[2], ':', player3Cards)
                print("cards for", newNames[3], ':', player4Cards)

                # player 1 turn
                print(newNames[0], ', You are the first to play')
                card1 = input('choose a card to throw:')
                while not isCardInList(player1Cards, card1):
                    print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                    card1 = input('choose a card to throw:')
                player1Cards.remove(card1)
                print("Leading Color Is:", leadingColor(card1))

                # player 2 turn
                print(newNames[1], ', Your turn to play')
                card2 = input('choose a card to throw:')
                while not isValidColor(card2, card1[0], isColorInList(player2Cards, card1[0])) \
                        or not isCardInList(player2Cards, card2):
                    print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                    card2 = input('choose a card to throw:')
                player2Cards.remove(card2)

                # player 3 turn
                print(newNames[2], ', Your turn to play')
                card3 = input('choose a card to throw:')
                while not isValidColor(card3, card1[0], isColorInList(player3Cards, card1[0])) \
                        or not isCardInList(player3Cards, card3):
                    print("the card you have selected is not valid. (the color is wrong or you don't have it)")
                    card3 = input('choose a card to throw:')
                player3Cards.remove(card3)

                # player 4 turn
                print(newNames[3], ', Your turn to play')
                card4 = input('choose a card to throw:')
                while not isValidColor(card4, card1[0], isColorInList(player4Cards, card1[0])) \
                        or not isCardInList(player4Cards, card4):
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

            print('Round is over. the looser is:', getLooserName(playersScore, names))
            whoLost = getLooserName(playersScore, names)
            roundNumber -= 1

    print('The winner is:', getWinnerName(playersScore, names))


p = ['Dor', 'Liran', 'Yoni', 'Ido']
Bridgini(p)
