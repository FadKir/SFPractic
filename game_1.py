import numpy as np
"""Просто угадываем рандомно число, выводим само число и 
   количкство попыток"""

number = np.random.randint(1, 101) # загадываем число
count = 0

# создаем бесконечную функцию пока не угодаем число
while True:
    count += 1 # обновляем количество попыток за каждый вод числа
    predict_number = int(input("Угадай число от 1 до 100"))

    if predict_number > number:
        print("Число должно быть меньше!")

    elif predict_number < number:
        print("Число должно быть больше!")

    else:
        print(f"Вы угадали число! Это число = {number}, за {count} попыток")
        break 
    # конец игры, выход из цикла