'''
Write a program able to play the "Guess the number" - game, where the number to be guessed is randomly chosen between 1 and 20. This is how it should work when run in a terminal:
Hello! What is your name?
KBTU

Well, KBTU, I am thinking of a number between 1 and 20.
Take a guess.
12

Your guess is too low.
Take a guess.
16

Your guess is too low.
Take a guess.
19

Good job, KBTU! You guessed my number in 3 guesses!

'''

import random
x=random.randint(1, 20)
name=input("Hello! What is your name? ")
guess=int(input("Well " + name + ", I am thinking of a number between 1 and 20. \nTake a guess. "))
i=1
while guess!=x:
    if (x>guess):
        print("Your guess is too low. ")
    elif (x<guess):
        print("Your guess is too high")
    i=i+1
    guess = int(input("Take a guess. "))
print("Good job, " + name + "! you guessed my number in " + str(i) + " guesses!")