n1 = int(input("Введите наименьшее число: "))
n2 = int(input("Введите наибольшее число: "))

print("Простые числа: ")
for number in range(n1, n2 + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)