from math import sqrt
n = int(input(f'Введите число n:'))

prime = True

i = 2
while i <= sqrt(n):
    if n % i == 0:
        prime = False
        break
    i += 1

if prime:
    print("Простое число")
else:
    print("Составное число")