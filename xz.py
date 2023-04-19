from colorama import Fore
from functools import reduce
print(Fore.CYAN)
n = int(input("Введите количество элементов массива: "))
arr = []
for i in range(n):
    arr.append(int(input(f"Введите число {i + 1}: ")))
    max_num = arr[0]
for i in range(1, n):
    if arr[i] > max_num:
            max_num = arr[i]
print("Максимальное значение в массиве:", max_num)
min_num = arr[0]
for i in range(1, n):
    if arr[i] < min_num:
            min_num = arr[i]
print("Минимальное значение в массиве:", min_num)
sum_nums = sum(arr)
avg_num = sum_nums / n
print('Среднее значение в массиве: ', avg_num)
x = int(input("Введите искомое значение: "))
found = -1
for i in range(n):
    if arr[i] == x:
        found = i
        break
print("Индекс искомого числа:", found)
count = n
print('Количество чисел в массиве(цикл):', count)
print('Количество чисел в массиве(функция):', len(arr))
sum_arr = sum(arr)
print("Сумма чисел в массиве(цикл):", sum_arr)
print("Сумма чисел в массиве(функция):", sum(arr))
prod_arr = 1
for i in arr:
    prod_arr *= i
print("Произведение чисел в массиве(цикл):", prod_arr)
prod_val = reduce(lambda x, y: x*y, arr)
print("Произведение чисел в массиве(функция):", prod_val)