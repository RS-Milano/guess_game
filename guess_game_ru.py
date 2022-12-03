from random import randint
from math import log, ceil
import os

def greetings():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Привет, это игра угадайка. Тебе нужно угадать число, которое загадал компьютер.")

def choose_the_range() -> int:
    limit: str = input("Давай выберем диапазон, в котором компьютер будет загадывать число (диапазон будет от 1 до выбранного числа).\nПожалуйста введи верхнюю границу диапазона (целое положительное число): ")
    while not (limit.isnumeric() and int(limit) > 0):
        os.system('cls' if os.name == 'nt' else 'clear')
        limit: str = input("Неверный ввод. Пожалуйста введите целое положительное число: ")
    os.system('cls' if os.name == 'nt' else 'clear')
    return int(limit)

def input_validation(str: str, num: int) -> bool:
    return str.isnumeric() and 0 < int(str) <= num

def get_valid_input(limit: int) -> int:
    guess: str = input(f"Угадай число в диапазоне до {limit}: ")
    while not input_validation(guess, limit):
        os.system('cls' if os.name == 'nt' else 'clear')
        guess: str = input(f"Неверный ввод. Пожалуйста введите целое положительное число до {limit}: ")
    return int(guess)

def game_ending(limit: int, guess: int, attempts: int) -> bool:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Вы угадали! Было загадано число {guess}. Вам понадобилось попыток: {attempts}.")
    print(f"Гарантированно угадать число в диапазоне [1, {limit}] можно за {ceil(log(limit, 2))} попыток.")
    return True if input("Будем играть еще?(да/нет): ") == "да" else False

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
                print(f"{guess} больше чем загаданное число.")
            else:
                print(f"{guess} меньше чем загаданное число.")
            guess: int = get_valid_input(limit)
            count_attempts += 1
        play_game = game_ending(limit, guess, count_attempts)
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
	game()