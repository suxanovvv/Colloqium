#44. Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
#своїм номером і при цьому кратні 3.

#Підготував Суханов Андрій Олександрович, 122Б

import numpy as np #Імпортуємо numpy, random.
import random

while True:
    #Генеруємо масив числами:
    A=np.array([random.randint(1,15) for i in range(15)])
    print('Масив: ', A)

    count=0
    for i in range(len(A)): #Отримаємо доступ до елементів масиву.
        if A[i]==i+1 and A[i]%3==0: #Берем порядковий номер, а не індекс, тому i+1.
            count+=1
    print('Кількість елементів, що збігаються із своїм порядковим номером і \
кратні 3 -', count)

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break
    