# Simple rock paper scissors program

import sys, random

wins = 0
losses = 0
ties = 0

while True:
    print('Welcome to rock paper scissors! You have ' + str(wins) + ' wins, ' + str(losses) + ' losses, and ' + str(ties) + ' ties.')
    while True:
        print('Your move! r = rock, p = paper, s = scissors, q = quit')
        playerInput = input()
        if playerInput == 'q':
            sys.exit()
        elif playerInput == 'r' or 'p' or 's':
            break
        else:
            print('Invalid input, try again.')
    
    if playerInput == 'r':
        print('ROCK versus... ')
    elif playerInput == 'p':
        print('PAPER versus... ')
    else:
        print('SCISSORS versus... ')
        
    computerInput = random.randint(1, 3)
    if computerInput == 1:
        print('ROCK')
        computerGuess = 'r'
    elif computerInput == 2:
        print('PAPER')
        computerGuess = 'p'
    else:
        print('SCISSORS')
        computerGuess = 's'
    
    if computerGuess == playerInput:
        print('Tied game!')
        tie = tie + 1
    elif playerInput == 'r' and computerGuess == 's':
        print('You win!')
        wins = wins + 1
    elif playerInput == 'p' and computerGuess == 'r':
        print('You win!')
        wins = wins + 1
    elif playerInput == 's' and computerGuess == 'p':
        print('You win!')
        wins = wins + 1
    elif playerInput == 'r' and computerGuess == 'p':
        print('You lose!')
        losses = losses + 1
    elif playerInput == 'p' and computerGuess == 's':
        print('You lose!')
        losses = losses + 1
    elif playerInput == 's' and computerGuess == 'r':
        print('You lose!')
        losses = losses + 1