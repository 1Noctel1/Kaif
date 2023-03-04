
xz = int(input(f'Выберите способ решения (1)-ариф или (2)-геом:'))
if xz == 1:
    a1 = int(input(f'Первая цифра:'))
    d = int(input(f'Разность:'))
    an = int(input(f'Кол - во цифр:'))
    yes = int(input(f'Выберите способ (1)-циклы или (2)-формулы:'))
    if yes == 1:
        print(a1)
        bp = a1
        summa = a1
        for i in range(a1):
            bc = bp + d
            print(bc)
            bd = bc + d
            print(bd)
            bt = bd + d
            print(bt)
            db = bt + d
            print(db)
            summa = bp + bc + bd + bt + db
            print(f'Сумма ариф прогрессии - {summa}')
    elif yes == 2:
        otvet = (2 * a1 + d * (an - 1))* an / 2
        print(f'Сумма ариф прогрессии = {otvet}')

else:
    t = int(input(f'Первая цифра:'))
    q = int(input(f'Знаменатель:'))
    bn = int(input(f'Кол - во цифр:'))
    no = int(input(f'Выберите способ (1)-циклы или (2)-формулы:'))
    if no == 1:
        print(t)
        bp = t
        sum = t
        for i in range(t, bn):
            bc = bp * q
            print(bc)
            sum = sum + bc
            bp = bc
        print(f'Сумма геом прогрессии = {sum}')
    elif no == 2:
        otvet = (t * (q ** bn - 1)) / q - 1
        print(f'Сумма геом прогрессии = {otvet}')
