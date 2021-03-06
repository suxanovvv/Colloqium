#59. Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
#чисел в ньому.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy.

while True:
    while True:
        #Ініціалізуємо масив нулями.
        A=np.zeros(10, dtype=int)

        for i in range(len(A)): #Отримуємо доступ до елементів матриці А.
            try: #Перевірка на входження чисел.
                A[i] =int(input('Введіть елементи масиву: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break
        #Для знаходження унікальних елементів, використаємо set та знайдемо \
        #її довжину.
        print('Кількість унікальних елементів у масиві: ', len(set(A)))

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break

        

