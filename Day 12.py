import random
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def user_attempts(answer,guess,turns):
    if guess>answer:
        print("Too high")
        return turns - 1
    elif guess<answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it:The answer was {answer}")

#make a funtion to set difficulty
def set_difficulty():
    level=input("Choose a difficulty.Type 'easy' or 'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
#choosing a number between 1 and 100
def game():
    print("Welcome to Number Guessing Game!")
    print("i'm thinking of a number between 1 and 100.")
    answer=random.randint(1,100)
    print(f"pssst,the correct answer is {answer}")
    turns=set_difficulty()

    guess=0
    while guess != answer:
        print(f"you have {turns} attempts remaining to guess the number.")
        guess=int(input("make a guess:"))
        turns = user_attempts(answer, guess, turns)
        if turns==0:
            print("You have run out of guesses,you lose.")
            return
        elif guess!=answer:
            print("Guess again.")
game()
























