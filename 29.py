#29. Знайти кількість парних елементів одновимірного масиву до першого
#зустрінутого числа рівного наперед заданому числу а.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy, random.
import random

while True:
    while True:
        #Генеруємо масив числами.
        A=np.array([random.randint(1,8) for i in range(10)])
        print('Масив: ', A)

        try: #вводимо "задане число" і перевіряємо, чи це справді число.
            a=int(input('Введіть число від 1 до 8: '))
        except ValueError:
            print('Input numbers!! ')
            break


        if 1<=a<=8: #Перевірка, чи є таке число, як ввів користувач у масиві.
            count=0
            for i in range(len(A)): #Отримаємо доступ до елементів масиву.
                if A[i]%2==0: #Якщо число парне, то парахуємо його, додавши 1.
                    count+=1
                if A[i]==a: #Рахуємо усі парні числа до вказаного числа.
                    break
            print('Кількість парних чисел, що зустрілись до вказаного числа: ', count)

        else: #Якщо число більше або менше, ніж те, яке потрібно, то :
            print('Ви не ввели число від 1 до 8. Введіть число від 1 до 8!')

        #Чи бажаєте повторити програму?
        result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
        if result=='1':
            continue
        break
    break
            

