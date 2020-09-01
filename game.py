import random

num = random.randint(1, 100)
guess1 = 0
while num != guess1:
    if guess1 == 0:
        guess1 = int(input('Guess a number between 1 & 100:', ))
    elif guess1 > num:
        print('Too High!')
        guess1 = int(input('Guess a number between 1 & 100:', ))
    elif guess1 < num:
        print('Too Low!')
        guess1 = int(input('Guess a number between 1 & 100:', ))

print("Got it: the number is {}".format(guess1))
