'''
Original Author: Dietel and Dietel
Modified: Nick Riblett
CIS 131
9/17/24
This progam will analyze the game of craps by keeping track of wins, losses, and what dice roll a win or loss occured
'''


import random

winDic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0}
lossDic = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0, 7:0, 8:0, 9:0, 10:0, 11:0, 12:0, 13:0, 14:0, 15:0, 16:0, 17:0, 18:0, 19:0, 20:0, 21:0, 22:0, 23:0, 24:0, 25:0}
keepGoing = 'y'
gameNum = 0

def roll_dice():
    """Roll two dice and return their face values as a tuple.
    
        input: none
        output: none
        return: dice roll as a tuple
    """

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)

    # pack die face values into a tuple
    return (die1, die2) 


def display_dice(dice):
    """Display one roll of the two dice.
    
        input: dice roll tuple
        output: each die roll and their sum
        return: nothing
    """

    # unpack the tuple into variables die1 and die2
    die1, die2 = dice  
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')


#Continue playing umtil desired number of games is reached
while keepGoing == 'y':
    
    # first roll
    die_values = roll_dice()  
    display_dice(die_values)
    diceRollNum = 1
    gameNum += 1

    # determine game status and point, based on first roll
    sum_of_dice = sum(die_values)

    # win
    if sum_of_dice in (7, 11):  
        game_status = 'WON'
        winDic[1] += 1

    # lose
    elif sum_of_dice in (2, 3, 12):  
        game_status = 'LOST'
        lossDic[1] += 1

    # remember point
    else:  
        game_status = 'CONTINUE'
        my_point = sum_of_dice
        print('Point is', my_point)

    # continue rolling until player wins or loses
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        diceRollNum += 1
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        #Allow data for 25+ rolls stored in 25
        if diceRollNum > 25:
            diceRollNum = 25
        else:
            diceRollNum = diceRollNum

        # win by making point
        if sum_of_dice == my_point:  
            game_status = 'WON'
            winDic[diceRollNum] += 1

        # lose by rolling 7
        elif sum_of_dice == 7:  
            game_status = 'LOST'
            lossDic[diceRollNum] += 1

    # display "wins" or "loses" message
    if game_status == 'WON':
        print('Player wins')
    else:
        print('Player loses')
    
    #Number of games
    if gameNum >= 100000:
        keepGoing = 'n'
    else:
        keepGoing = 'y'

gamesWon = 0
gamesLost = 0

#Total games win
for wins in winDic.values():
    gamesWon += wins

#Total games lost
for loss in lossDic.values():
    gamesLost += loss

#Print resultts
print(f"\nThe percentage of games won is {(gamesWon / gameNum) * 100:.2f}%")
print(f"The percentage of games lost is {(gamesLost / gameNum) * 100:.2f}%\n")
print(f"{'Resolved %':>19} {'Cumaltive %':>16}")
print(f"{'Rolls':<7} {'on this roll':>7} {'of the game':>15}")

precentTotal = 0

#Calculate percentage of wins/losses on specific roll and print
for i in range(25): 
    precentTotal += ((winDic[i + 1] + lossDic[i + 1]) / gameNum) * 100
    print(f"{i + 1:>3} {((winDic[i + 1] + lossDic[i + 1])  / gameNum) * 100 :>12.2f}% {precentTotal :>15.2f}%")


