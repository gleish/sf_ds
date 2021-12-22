''' Игра "Угадай число" '''

import numpy as np

def random_predict(number: int=1) -> int:
    """Рандомное угадывание компьютером числа в диапазоне от 1 до 100 включительно

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # Очередная попытка компьютера угадать число
        if predict_number == number:
            break # Конец игры и выход из цикла
    
    # print(f'Количество попыток в очередном цикле {count}')
    return(count) # Возврат количества попыток


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм-угадывальщик

    Args:
        random_predict ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # Фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # Загадали список чисел
    # print(random_array)
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш аглоритм угадывает число от 1 до 100 в среднем за {score} попыток')
    return(score)

if __name__ == '__main__': # Если файл будет импортирован как библиотека в другой, эта команда не будет выполнена 
    # RUN
    score_game(random_predict)