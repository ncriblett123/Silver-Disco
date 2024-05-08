#This is where BlackJack will Be
#This is also a test 
#This is where BlackJack will Be
#This is also a test 
#My attempt at creating blackjack
import itertools
import random


def main():
    playersHand = []
    points = []
    hand = []
    bet = []
    deck = []
    deckCount = 1
    counter = 0
    play = 'y'

    for i in range(deckCount):
        deck = DeckCreation(deck)
    for i in range(7):
        random.shuffle(deck)
    playerNum = int(input("How many players?: "))
    
    for i in range(playerNum + 1): #Creates an empty hand for each player and the dealer
        playersHand.append(i)
    for i in range(playerNum + 1): #Creates an empty points hand for each player and the dealer
        points.append(i)
    for i in range(playerNum + 1): #Deals the cards to players and dealer
        hand = deck[i], deck[i + (playerNum + 1)]
        hand = list(hand)
        playersHand[i] = hand
        deck.pop(i)
        deck.insert(i, ' ')
        deck.pop(i+(playerNum + 1))
        deck.insert((i + playerNum + 1), ' ')
        counter = counter + 2

    del deck[:counter]
    points = CreateHand(playersHand)
    deck, points, playersHand, bet = PlayHand(deck, points, playersHand, bet)
    if points[-1] == 21:
        print(f"Dealer had blackjack")
        play = 'n'
        #for i in range(playerNum):
            #bet[i][0] = bet[i][0] - bet[i][1]

    while play == 'y':
        DealerPlay(deck, playersHand, points, bet)
        play = 'n'
    print("Thanks for playing")


def PlayHand(deck, points, hand, bet): 
    player = 1
    newCard = []

    for i in range(len(hand) - 1):
        play = 'y'
        cardPoints = 0
        p = 0
        if points[i] == 99:
            play = 'n'
        while play == 'y':
            print(f"Player {player} you have:", end = ' ')
            for n in range(1):
                for j in range(len(hand[i])):
                  print(f" {hand[i][j]}", end = ' ')
            print()
            action = input(("Would you like to hit, stand, or double?(h/s/d): "))
            print()
            if action == 'h':
                newCard = deck[0]
                print(newCard)
                input()
                deck.pop(0)
                hand[i].append(newCard)
                cardPoints = PointTotal(newCard)
                if points[i] > 11 and cardPoints == 11:
                    cardPoints = 1
                points[i] = points[i] + cardPoints
                for k in range(len(hand[i])):
                    if points[i] > 21 and ('A' in hand[i][k]) and p == 0:
                        points[i] = points[i] - 10
                        p = 1

                if points[i] > 21:
                    print(f"{points[i]} points, you busted")
                    input()
                    points[i] = 0
                    play = 'n'
                    player = player + 1
            if action == 's':
                play = 'n'
                player = player + 1
            #if action == 'st':
                
            #if action == 'd':
                #bet[i][1] = bet[i][1] * 2

    
    return(deck, points, hand, bet)

def CreateHand(playersHand):
    player = 1
    points = 0
    pointReturn = 0
    playerPoints = []

    for i in range(len(playersHand) - 1):
        print(f"Player{player} has a {playersHand[i][0]} and a {playersHand[i][1]}")
        input()
        player = player + 1
    print(f"Dealer had a face up {playersHand[(len(playersHand) - 1)][0]} and a face down card")
    input()

    for i in range(player):
        playerPoints.append(i)

    for i in range (player):
        for j in range(2):
            pointReturn = PointTotal(playersHand[i][j])
            points = points + pointReturn
        playerPoints[i] = points 
        points = 0
        if playerPoints[i] == 21:
            print(f"Player {i + 1} you got Blackjack!")
            playerPoints[i] = 99 
    
    
           
    return(playerPoints)
    
def PointTotal(hand):
    points = 0 
    TENS = ['10 Spades', '10 Hearts', '10 Diamonds', '10 Clubs']
    
    if hand[0] == 'A':
        points = 11
    elif hand[0] == 'K' or hand[0] == 'Q' or hand[0] == 'J':
        points = 10
    elif hand in TENS:
        points = 10
    else:
        points = int(hand[0])

    return(points)

def DeckCreation(cards):
    ranks = ["A", '2', '3', '4', '5', '6', '7', '8', '9', '10', "J", "Q", "K"]
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    for rank in ranks:
        for suit in suits:
            new_card = (rank, suit)
            new_card = ' '.join(new_card)
            cards.append(new_card)
    return(cards)

def DealerPlay(deck, playerHand, points, bet):
    newCard = []
    player = 1
    p = 0

    print(f"Dealer shows a {playerHand[-1][1]}")
    input()
    
    
    while points[-1] <= 17:
        cardPoints = 0
        newCard = deck[0]
        print('Dealer pulls a ', newCard)
        input()
        deck.pop(0)
        playerHand[-1].append(newCard)
        cardPoints = PointTotal(newCard)
        if points[-1] > 11 and cardPoints == 11:
            cardPoints = 1
            points[-1] = points[-1] + cardPoints
        for k in range(len(playerHand[-1])):
            if points[-1] > 21 and ('A' in playerHand[-1][k]) and p == 0:
                    points[-1] = points[-1] - 10
                    p = 1
        points[-1] = points[-1] + cardPoints
    print(f"Dealer has a", end = ' ')
    for i in range(len(playerHand[-1])):
        print(playerHand[-1][i], end = ' ')
    print(':', end = ' ')
    print(f'{points[-1]} points')
    input()
    if points[-1] <= 21:
        for i in range(len(playerHand) - 1):
            if points[i] > points[-1]:
                print(f"Player {player} you have {points[i]} points you win!")
                input()
                #bet[i][0] = bet[i][0] + bet[i][1]
                #print("{bet[i][1]} chips have been added")
            elif points[i] < points[-1]:
                print(f'Player {player}, you lost with {points[i]} points')
                #bet[i][0] = bet[i][0] - bet[i][1]
            player = player + 1
                        
    for i in range(len(playerHand) - 1):        
        if points[-1] > 21 and points[i] != 0:
            print("Dealer busted")
            if points[i] != 0:
                print(f"Player {i + 1}, you win")
                input()
                #bet[i][0] = bet[i][0] + bet[i][1]

        if points[-1] > 21 and points[i] == 0:
            print("Both player and dealer busted")
            #bet[i][0] = bet[i][0] - bet[i][1]
        if points[-1] == points[i]:
            print(f"Player {i + 1} and dealer push")







main()
