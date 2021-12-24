''' Игра "Угадай число" '''


''' 

Полное описание игры "Угадай число" - в файле game_v2_1_fast.ipynb (Jupiter Notebook).

В этой программе осуществляются 2 типа игры:

- поиск числа случайным выбором 
- и поиск путем деления диапазона пополам. 

В обоих случаях выводится среднее количество попыток при 1000 циклах. 

В конечном итоге сравниваются результаты.

'''

import numpy as np

min_number = 1
max_number = 100

def random_predict(number: int=1) -> int:
    """Случайный выбор числа в диапазоне от 1 до 100 включительно

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    global min_number
    global max_number
    min_n = min_number
    max_n = max_number
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(min_n, max_n+1) # Очередная попытка компьютера угадать число
        
        if predict_number == number:
            break # Конец игры и выход из цикла
    
    return count # Возврат количества попыток


def round_number(number: float, digits: int=0):  
    '''Честное математическое округление через строчное представление
    
    Автор: Алексей Кияница, Петрозаводск, очень умный человек, рад Вашим письмам, телеграммам, переводам
    
    Args:
        number (int, float): Округляемое число
        digits (int, optional): Разрядность округления, где 0 - до целого
        
    Returns:
        round_num (float): Округленное число
    '''
    number = str(float(number))
    round_num = ''
    dot_i = None # Номер позиции десятичного разделителя
    
    for i in range(0, len(number)): 
        if (number[i] == '.' or number[i] == ','):
            dot_i = i
    
    decimal_part = len(number) - (dot_i + 1)

    round_up = 0
    if digits >= decimal_part: # Если в строковом числе десятичных разрядов меньше или равно, чем желаемый порядок округления
        round_up = 0
        number = number + (digits - decimal_part + 1)*'0'
        
    if digits < decimal_part and int(number[dot_i + digits + 1]) > 4: # Если десятичных разрядов больше, чем желаемый порядок округления
        round_up = 1
        
    if digits == 0: 
        
        number = '0' + number # Добавление 'виртуального' нулевого разряда перед числом для создания среза до округляемого числа     
        round_num = float(int((str(number[:(dot_i - 1 + 1)]))) * (10**(dot_i - 1)) + int(number[dot_i - 1 + 1]) + round_up)
        
    if digits > 0: 
        round_num = float(number[:(dot_i + digits)] + str(int(number[dot_i + digits]) + int(round_up)))
        
    return round_num           


def devision_predict(number: int = 1) -> int:  
    """Поиск числа делением диапазона от 1 до 100 включительно пополам
    
    Автор: Алексей Кияница, Петрозаводск, очень умный человек, рад Вашим письмам, телеграммам, переводам
    
    Используется метод ловли льва в прериях: слушаем, с какой стороны рычит, и делим прерию пополам,
    после чего идем в рычащую половину и делим ее пополам, и в какой-то момент встретимся на радость льву
    
    Args: не передаются; применяется величина 50% (в коде - 50/100)
    
    Returns:
        int: Число попыток
    """

    global min_number
    global max_number
    min_n = min_number
    max_n = max_number

    count = 0
    
    predict_number = min_n + 1
    
    #print()
    #print(f'Старт цикла угадывания: number = {number}, predict_number = {predict_number}')
    #print()
         
    while True:
        count += 1
        
        # print(f'number = {number}, min_n = {min_n}, max_n = {max_n}')
        
        if count > 10: # Отладочный блок: убеждаемся в том, что не вошли в избыточно долгий цикл
            print()
            raise ValueError(f'Программа вошла в бесконечный цикл: \n \
                number = {number} \n \
                min_n = {min_n} \n \
                max_n = {max_n} \n \
                predict_number = {predict_number}')
        
        # print(f'                                               Предсказание predict_number = {predict_number}')
        
        # Отладка
        #pause = None
        #pause = input('Продолжить? 0 = Нет ')
        #if pause == '0': break
                
        if (predict_number == number) and (min_n <= predict_number <= max_n):
            
            #print(f'Число {number} угадано за {count} попыток!')
            break # Число угадано! Конец игры и выход из цикла
        
        elif (predict_number != number) and (round_number(max_n - min_n, 0) == 1) and (min_n <= predict_number <= max_n):
            
            if predict_number == min_n:
                predict_number = max_n
            elif predict_number == max_n:
                predict_number = min_n
        
        elif (predict_number != number) and (round_number(max_n - min_n, 0) > 1) and (min_n <= predict_number <= max_n):
            
            predict_number = min_n + (max_n - min_n)/2
            predict_number = int(round_number(predict_number, 0))
            
            if (predict_number < number):
                min_n = int(round_number(predict_number, 0))
                continue
            elif (predict_number > number):
                max_n = int(round_number(predict_number, 0))
                continue
        
        else:
            # Отладочный блок: убеждаемся, что predict_number выбирается из диапазона, иначе выводим ошибку
            if (predict_number < min_n) or (predict_number > max_n): 
                print('Predict_number is out of range: ', min_n, max_n, predict_number)
                break # Конец игры и выход из цикла
    
    return count # Возврат количества попыток


def score_game(predict_function) -> int:
    """За какое количество попыток в среднем за 1000 подходов наш алгоритм-угадывальщик угадывает число

    Args:
        predict_function ([type]): Функция угадывания

    Returns:
        int: Среднее количество попыток
    """
    
    global min_number
    global max_number
    min_n = min_number
    max_n = max_number
    
    count_ls = []
    # np.random.seed() # Фиксируем сид для воспроизводимости
    random_array = list(np.random.randint(min_n, max_n+1, size=(1000))) # Загадали список чисел
    #print('Загаданные числа: ', random_array)
    
    for number in random_array:
        count_ls.append(predict_function(number))
    
    #print('Количество попыток', count_ls)    
    score = int(np.mean(count_ls))
    print(f'Этот аглоритм угадывает число в среднем за {score} попыток')
    return score


def winner_announcement():
    """Вывод результатов для ознакомления

    Returns:
        [None]: Функция ничего не возвращает, а только печатает выводы
    """
    

    global min_number
    global max_number
    
    print()
    print(f'СРАВНЕНИЕ АЛГОРИТМОВ УГАДЫВАНИЯ ЧИСЛА ИЗ ДИАПАЗОНА {min_number}-{max_number}')
    print()
    print('Алгоритмы: \n     1. Случайный выбор числа \n     2. МОЙ АЛГОРИТМ: Поиск числа делением диапазона пополам')
    print()
    
    print("1. Случайный выбор числа:")
    #score_game(random_predict)
    res_1 = score_game(random_predict)
    print()
    print("2. Поиск числа делением диапазона:")
    #score_game(devision_predict)
    res_2 = score_game(devision_predict)
    print()
        
    if res_2 < res_1:
        winner_name = '"Поиск числа делением диапазона"'
        winner_count = res_2
        looser_count = res_1
    elif res_1 < res_2:
        winner_name = '"Случайный выбор числа"'
        winner_count = res_1
        looser_count = res_2
    else: 
        winner_name = 'Спорт! И Дружба!'
    
    print(f'В соревновании победил алгоритм {winner_name} со счетом {winner_count} против {looser_count}')
    print()
        
    if res_2 < 20 or res_1 < 20:
        verdict = 'очень хорош!'
    if res_2 < 14 or res_1 < 14:
        verdict = 'великолепен!'
    if res_2 < 7 or res_1 < 7:
        verdict = 'потрясает мир и затмевает Солнце своим сиянием!'
    
    print(f'Результат победителя {winner_name} {verdict}')
    print()
    
    return None
    
    
if __name__ == '__main__': # Если файл будет импортирован как библиотека в другой, эта команда не будет выполнена 
    # RUN

    winner_announcement()