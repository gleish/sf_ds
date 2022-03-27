def round_number(number, digits):

    
    '''НЕ РАБОТАЕТ ФУНКЦИЯ ОКРУГЛЕНИЯ В ТОМ СЛУЧАЕ, 
    ЕСЛИ В ТРЕХ РАЗРЯДАХ ПОДРЯД В КОНЦЕ ИДУТ ЧИСЛА 9 - 
    9 ОКРУГЛЯЕТСЯ ДО 10, НО РАЗРЯД ВЛЕВО НЕ ПРИБАВЛЯЕТСЯ
    
    5,598 ОКРУГЛИЬ ДО 2 РАЗР = 5Б,6, А НЕ 5,510
    
    '''
    
    
    '''
        
    Честное математическое округление через строчное представление
    
    Автор: Алексей Кияница, Петрозаводск, очень умный человек, рад письмам, телеграммам и Вашим переводам
    
    Args:
        number (int, float): Округляемое число
        digits (int, optional): Разрядность округления, где 0 - до целого
        
    Returns:
        round_num (float): Округленное число
    '''
    
    arсhived = number
    number = str(float(number))
    round_num = ''
    
    print()
    print(f'Округляемое число = {number}')
    print(f'Округлить до {digits} разрядов после разделителя')

    dot_i = None # Номер позиции десятичного разделителя
    
    for i in range(0, len(number)): 
        if (number[i] == '.' or number[i] == ','):
            dot_i = i
    
    decimal_part = len(number) - (dot_i + 1)
    
    print(f'Десятичных разрядов = {decimal_part}')
    print(f'Разделитель {number[dot_i]} находится в позиции {dot_i}')
    
    round_up = 0
    if digits >= decimal_part: # Если в строковом числе десятичных разрядов меньше или равно, чем желаемый порядок округления
        round_up = 0
        number = number + (digits - decimal_part + 1)*'0'
        
        print(f'Округляемое число с учетом добавляемых разрядов = {number}')
        
    if digits < decimal_part and int(number[dot_i + digits + 1]) > 4: # Если десятичных разрядов больше, чем желаемый порядок округления
        round_up = 1
    
    print(f'Округляющее число {number[dot_i + digits + 1]} находится в позиции {dot_i + digits + 1}')
        
    if digits == 0: 
        
        number = '0' + number # Добавление 'виртуального' нулевого разряда перед числом для создания среза до округляемого числа
        
        #'''
        
        print()
        print('Проверка округления')
        print(f'Срез до округляемой цифры number[:(dot_i - 1 + 1)] = {number[:(dot_i - 1 + 1)]}')
        print(f'Умножение на 10**(dot_i - 1) = {10**(dot_i - 1)}')
        print(f'Округляемая цифра number[dot_i - 1 + 1] = {number[dot_i - 1 + 1]}')
        print(f'Фактор округления round_up = {round_up}')
        print(f'Округленное число round_num = {round_num}')
        print()
        
        #'''
        
        round_num = float(int((str(number[:(dot_i - 1 + 1)]))) * (10**(dot_i - 1)) + int(number[dot_i - 1 + 1]) + round_up)
        
        print(f'Срез до округляемой цифры = {number[:(dot_i - 1)]}')
        print(f'Округляемая цифра = {number[dot_i - 1]}')
        print(f'Фактор округления вверх = {round_up}')
        print()
    
    if digits > 0: 
        round_num = float(number[:(dot_i + digits)] + str(int(number[dot_i + digits]) + int(round_up)))
        
        print(f'Срез до округляемой цифры = {number[:(dot_i + digits)]}')
        print(f'Округляемая цифра = {number[dot_i + digits]}')
        print(f'Фактор округления вверх = {round_up}')
        print()
    
    print(f'Изначальное оругляемое число = {arсhived}')
    print(f'Порядок округления = {digits}')    
    print(f'Конечное округленное число = {round_num}')
    print(f'Type(round_num) = {type(round_num)}')
    print()
    return round_num            


import numpy as np
# print(f'Округленное число = {round_number(np.random.randint(1, 1000)/10000, 0)}')
print(f'Округленное число = {round_number(0.56897, 4)}')        
print()
