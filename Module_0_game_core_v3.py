import numpy as np
import random

def game_core_v3(number):
    count = 1                           #Устанавливаем рандомное число
    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number >= predict:            # Начинаем перебирать под нужнее число, увеичив шаг подбора
            predict += 5
        elif number <= predict:
            predict -= 1
    return(count)                       # выход из цикла, если угадали


def score_game(game_core):
    count_ls = []                       #запускаем цикл 1000раз, чтобы узнать за сколько в среднем программа выполняет программу
    np.random.seed(1)                   # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return (score)
score_game(game_core_v3)