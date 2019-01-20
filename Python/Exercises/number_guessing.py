# Guessing number
import random
number = random.randint(1, 9)
guess = 0
count = 0
while guess != number and guess != 'exit':

    guess = input('Guess a number between 1 to 9: ')
    if guess == 'exit':
        break
    count += 1
    guess = int(guess)

    if guess > 9 or guess < 1:
        print(
            f' You Guessed {guess}, Guess the numbers between 1 to 9')
        continue
    elif guess > number:
        print('Guess lower')
    elif guess < number:
        print('Guess higher')

    else:
        print(f'Number {guess}: is correct. You took {count} trie(s)')
