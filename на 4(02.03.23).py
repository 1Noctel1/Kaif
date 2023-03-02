from statistics import mean
a = float(input(f'Первое значение:'))
b = float(input(f'Второе значение:'))
c = float(input(f'Искомое значение:'))
it = (a, b)
print(mean(it))
if mean(it) == c:
    print(f'True')
else:
    print(f'Пожалуйста, введите другие значения.')