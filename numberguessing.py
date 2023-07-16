#Simple number guessing game

import random

number = random.randint(1, 10)

print('I am thinking of a number between 1 and 10. How many guesses would you like?')

guesses = input()

for i in range(1, int(guesses) + 1):
    print('guess a number:')
    guess = int(input())
    if (guess == number):
        print('you guessed it!')
        break
    else:
        print('incorrect.')

if (guess == number):
    print('good job, you guessed the number in ' + str(i) + ' guesses!')
else:
    print('you failed to guess the number in ' + guesses + ' guesses :(')