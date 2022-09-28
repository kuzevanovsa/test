"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def predict(number: int = 1) -> int:
    """Function to predict a random number in 20 or less tries

    Args:
        number (int, optional): a predict number. Defaults to 1.
        
    Returns:
        int: count of tries
    """
    
    count = 0
    min_number = 1 # нижняя граница поиска
    max_number = 101 # верхняя граница поиска

    while True:
        count += 1

        predict_number = (max_number + min_number) // 2 # предполагаемое число
            
        if number == predict_number:
            break  # выход из цикла если угадали
        elif number > predict_number:
            # если число больше предполагаемого, изменяем нижнюю границу
            min_number = predict_number
        else:
            # если число меньше предполагаемого, изменяем верхнюю границу
            max_number = predict_number
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score 


if __name__ == "__main__":
    # RUN
    score_game(predict)
