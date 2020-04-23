#45. Перетин даху має форму півкола з радіусом R м. Сформувати таблицю,
#яка містить довжини опор, які встановлюються через кожні R / 5 м.

#Підготував Суханов Андрій Олександрович, 122Б.

import math

#Трикутник, що утворений точкою на колі і кінцями діаметру є прямокутний,
#а висота, опущена з прямого кута є середнє геометричне відрізків діаметра,\
#на які вона його ділить.
#Тому у відповіді перша і остання опора співпадатимуть, друга і передостання,\
#і тд. Середня опера буде дорвінювати радіусу кола.

while True:
    R=int(input('Введіть радіус: '))
    diametr=2*R #Відразу знайдемо діаметр.

    every_R=R/5 #значення кожних 5 метрів.
    count=0
    supp=0 #Порядковий номер опори.

    while count<diametr-every_R:
        count+=every_R
        supp+=1
        print(f'Опора {supp}: ', math.sqrt(count*(diametr-count)))

    #Чи бажаєте повторити програму?
    result=input('Введіть "1", щоб продовжити, інше - для виходу: ')
    if result=='1':
        continue
    break
    
