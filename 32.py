#32. Змінній t привласнити значення істина, якщо в одновимірному масиві є
#хоча б одне від’ємне і парне число.

#Підготував Суханов Андрій Олександрович, 122Б.

import numpy as np #Імпортуємо numpy, random.
import random

while True:
    #Генеруємо масив числами:
    A=np.array([random.randint(-10,10) for i in range(10)])

    print('Масив: ', A)

    t=False #поки присвоємо змінній t значення False.
    for i in range(len(A)): #Отримаємо доступ до елементів масиву.
        if A[i]%2==0 and A[i]<0: #Якзо елемент парний і від'ємний, то істина.
            t=True
    print(t)

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break
