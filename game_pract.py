"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Создаем функцию для определения кол.-ва попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0 # присваиваем нулевое значение, переменой куда будем заносить кол.-во попыток
    lower_val = 1  # присваиваем значение, соответствующее нижней границе диапазона поиска
    upper_val = 101  # присваиваем значение, соответствующее верхней границе диапазона поиска +1
    
    # создаем бесконечную функцию пока не будет угадано число
    while True:
        average_number = (lower_val + upper_val)//2
        count += 1
        if average_number == number:
            break  # выход из цикла если угадали
        elif number > average_number:
            lower_val = average_number  # перезаписываем значение нижней граници 
        else:
            upper_val = average_number # перезаписываем переменную значение верхней граници

# выводим кол.-во попыток
    return count

def score_game(game_core_v3) -> int:
    """За какое кол.-во попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = [] # создаем пустой лист с кол.-вом попыток
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array: 
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) # определяем среднее из значение из списка количеств попыток
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == "__main__":
    # RUN
    score_game(game_core_v3)