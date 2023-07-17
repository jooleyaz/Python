# Collatz function: if a number is even, collatz divides it by two and returns. if odd, collatz prints and returns the number, times 3, plus 1.
# The main function prompts the user to type in an integer, then calls collatz until the value is 1.

def collatz(number):
 if number % 2 == 0:
  number = number // 2
  print(number)
  return number
 else:
  number = number * 3 + 1
  print(number)
  return number

print('Hi! Please enter any integer number, and the final value will be 1 as aligned with the collatz function.')

userInput = int(input())

while userInput > 1:
 userInput = collatz(userInput)