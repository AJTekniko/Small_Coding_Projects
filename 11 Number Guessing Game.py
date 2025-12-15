from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user_guess, actual_num, turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_num:
        print("Too high.")
        return turns - 1
    elif user_guess < actual_num:
        print("Too low.")
        return turns - 1
    else:
        print(f"Congratulations! The number was {actual_num}")

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_num = randint(1, 100)
    #print(f"The correct answer is {secret_num}")

    turns = set_difficulty()

    guess = 0
    while guess != secret_num:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, secret_num, turns)
        if turns == 0:
            print(f"You've run out of guesses, you lose. The correct answer was {secret_num}")
            return
        elif guess != secret_num:
            print("Guess again.")

game()
