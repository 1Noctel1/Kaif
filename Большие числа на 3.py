number = input("Введите число: ")
digits = list(number)
print("Отдельные цифры:", digits)
sum = 0
pr = 1
max = float("-inf")
min = float("inf")
for digit in digits:
    d = int(digit)
    sum += d
    pr *= d
    if d > max:
        max = d
    if d < min:
        min = d
print("Сумма цифр:", sum)
print("Произведение цифр:", pr)
print("min:", max)
print("max:", min)
