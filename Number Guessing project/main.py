from random import randint
from art import logo
print(logo)
EASY_LEVEL_TURNS=10
HARD_LEVELS_TURNS=5
turns=0
# choosing a random number between 1 and 100
# function to check user guess against actual number
def check_answer(user_guess,actual_number,turns):
    if user_guess>actual_number:
        print("Too high")
        return turns-1
    elif user_guess<actual_number:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it, the actual answer was {actual_number}")


# function to set difficulty
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard'")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVELS_TURNS
def game():

    print("Welcome to Number Guessing Game")
    print("I m thinking of a number between 1 and 100.")
    answer=randint(1,100)
    print(f"Pstt,the correct answer is {answer}")

    turns=set_difficulty()

    guess=0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess=int(input("Make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you have run out of guesses,you loose")
            return
        elif guess!=answer:
            print("guess again")
game()
