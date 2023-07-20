# number guessing game :D
# computer chooses number between 1 and 500 (tbd)
# computer will output "higher" or "lower" in accordance with the user's input(s)
# after user guesses number, prompted to play again

import random # for rng
from os import system # for clear() function
from time import sleep # for sleep() function
def clear(): # the clear() function in question (just clears the output/console screen)
    _ = system('cls')

def main():
    stage1()

def is_guess_correct(user_guess, num_ans):
    if user_guess == num_ans:
        input("whoa, bang on!! you guessed my super secret number of " + str(num_ans) + ", congrats :')") # win condition achieved, returns didWin bool as True
        return True
    elif user_guess > num_ans:
        input("too high!")
    else:
        input("too low!")
    return False

def actualGame():
    didWin = False
    numAns = random.randint(1, 500)
    guesses = 10
    pluralG = "es"
    while guesses > 0:
        clear()
        usrGuess = int(input("guess a number, you have " + str(guesses) + " guess" + "es"*(guesses>1) + " left\n"))
        if (is_guess_correct(usrGuess, numAns)):
            return True
        guesses -= 1
    return False

def stage1():
    print("welcome to toxx's epic number guessing game")
    sleep(1.5)
    print("i am now selecting a random number, you should try to guess it based on whether i say 'higher' or 'lower' based on your guess")
    sleep(2.2)
    print("i have now selected a number! press enter when ready")
    input()
    clear()
    while True:
        didWin = actualGame()
        clear()
        if didWin == True:
            YorNFunc(input("nice work figuring it out, want to try again? Y/N\n"))
        else:
           YorNFunc(input("uff bad luck champ, wanna give it another ago?"))

def YorNFunc(YorN):
    YorN = YorN[0].lower()
    if YorN == "n":
        input("no worries, til next time B)")
        exit
    elif YorN == "y":
        input("cool, putting you back in now")
    else:
        input("clearly was not what i asked for but alright, woe upon ye")
        exit
    return

main()