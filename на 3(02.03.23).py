
xz = int(input(f'Выберите способ решения (1) или (2):'))
if xz == 1:
    a1 = int(input(f'Первая цифра:'))
    d = int(input(f'Разность:'))
    an = int(input(f'Вторая цифра:'))
    for i in range(a1, an, d):
        print(i)

else:
    t = int(input(f'Первая цифра:'))
    q = int(input(f'Знаменатель:'))
    bn = int(input(f'Вторая цифра:'))
    print(t)
    bp = t
    sum = t
    for i in range(t, bn):
        bc = bp * q
        print(bc)
        sum = sum + bc
        bp = bc
    print(sum)