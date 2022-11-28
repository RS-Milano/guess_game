from random import randint
from math import log, ceil
import os

def greetings():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Hi, it is a guess game. You need to guess a natural number that the computer guessed.")

def choose_the_range() -> int:
    limit: str = input("Let's choose the range in which computer will guess the number (range will be from 1 to n).\nPlease input a natural number: ")
    while not (limit.isnumeric() and int(limit) > 0):
        os.system('cls' if os.name == 'nt' else 'clear')
        limit: str = input("Incorrect input. Please input a natural number: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return int(limit)

def input_validation(str: str, num: int) -> bool:
    return str.isnumeric() and 0 < int(str) <= num

def get_valid_input(limit: int) -> int:
    guess: str = input(f"Guess a natural number up to {limit}: ")
    while not input_validation(guess, limit):
        os.system('cls' if os.name == 'nt' else 'clear')
        guess: str = input(f"Incorrect input. Please input a natural number up to {limit}: ")
    return int(guess)

def game_ending(limit: int, guess: int, attempts: int) -> bool:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"You are right. The hidden number is {guess}. You guessed right in {attempts} tries.")
    print(f"It was guaranteed to guess any hiiden number in range [1, {limit}] in {ceil(log(limit, 2))} attempts.")
    return True if input("Whould you like to play again?(y/n): ") == "y" else False

def game():
    greetings()
    play_game = True
    while play_game:
        limit: int = choose_the_range()
        hidden_number: int = randint(1, limit)
        count_attempts: int = 1
        guess: int = get_valid_input(limit)
        while hidden_number != guess:
            os.system('cls' if os.name == 'nt' else 'clear')
            if guess > hidden_number:
                print(f"{guess} is more than hidden number.")
            else:
                print(f"{guess} is less than hidden number.")
            guess: int = get_valid_input(limit)
            count_attempts += 1
        play_game = game_ending(limit, guess, count_attempts)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	game()