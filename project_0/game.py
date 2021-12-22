''' Игра "Угадай число" '''

import numpy as np

number = np.random.randint(0, 101) # Загадываем число от 1 до 100 включительно

# Количество попыток угадывания
count = 0

while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number and 0 < predict_number < 101:
        print(F'Число должно быть меньше {predict_number}')

    elif predict_number < number and 0 < predict_number < 101:
        print(F'Число должно быть больше {predict_number}')
        
    elif predict_number == number and 0 < predict_number < 101:
        print(f'Вы угадали число {number} за {count} попыток')
        break # Конец игры и выход из цикла
    
    else:
        print('Досрочный выход из игры')
        break # Конец игры и выход из цикла


    

