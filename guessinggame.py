import random
EASY_LEVEL_TURNS=5
HARD_LEVEL_TURNS=10


def user_attempts(attempts,guess,turns):
    if attempts>guess:
        print("Too high")
        return turns-1
    elif attempts<guess:
        print("Too Low")
        return turns-1
    else:
        print(f"you got it!The answer was  {guess}")
def set_difficulty():
    level=input("Choose difficulty.Type 'Easy' or 'Hard.")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
def game():
    print("Welcome to Number Guessing Game!")
    print("i'm thinking of a number between 1 and 100.")
    guess=random.randint(1,100)
    print(f"pssst,the correct answer is {guess}")
    turns=set_difficulty()

    attempts=0
    while attempts != guess:
        print(f"you have {turns} attempts remaining to guess the number.")
        attempts=int(input("make a guess:"))
        turns = user_attempts(attempts, guess, turns)
        if turns==0:
            print("You have run out of guesses,you lose.")
            return
        elif attempts!=guess:
            print("Guess again.")
game()


