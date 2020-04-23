#54. Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
#однаковими значеннями.

#Підготував студент 1-го курсу групи 122Б, Суханов Андрій Олександрович.

import numpy as np #Імпортуємо numpy.

while True:
    while True:
        #Ініціалізуємо масив нулями.
        A=np.zeros(8, dtype=int)

        for i in range(len(A)): #Отримуємо доступ до елементів матриці А.
            try: #Перевірка на входження чисел.
                A[i] =int(input('Введіть елементи масиву: '))
                continue
            except ValueError:
                print('Input numbers!! ')
                break

        A_unique=set(A) #За допомогою set ми видаляємо елементи, що повторюються\
        #і якщо довжина масиву А не співпаде з її множиною (set), то у масиві є\
        #елементи, що повторюються.

        if len(A_unique)==len(A):
            print('Немає однакових елементів')
        else:
            print('У масиві є елементи з однаковими значеннями!')

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
