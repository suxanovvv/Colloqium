#23. Знайти суму всіх елементів масиву цілих чисел, які менше середнього
#арифметичного елементів масиву. Розмірність масиву - 20. Заповнення масиву
#здійснити випадковими числами від 150 до 300.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy, random.
import random

while True:
    #Генеруємо елементи масиву числами.
    A=np.array([random.randint(150,300) for i in range(20)])
    print('Масив: ',A)

    average=np.mean(A) #знаходимо середнє значення масиву.
    print('Середнє значення усіх елементів масиву: ', average)
    print()

    summa=0
    for i in range(len(A)): #Отримаємо доступ до елементів масиву.
        if A[i]<average: #Якщо елемент менше, ніж середнєзначення, то:
            summa+=A[i] #додаємо елемент у лічильник.
            print(f'Числа, менші від {average} - {A[i]}.')
    print()
    print('Знайдемо суму цих чисел: ')
    print(f'Сума елементів, менших від {average} - {summa}.')

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break
