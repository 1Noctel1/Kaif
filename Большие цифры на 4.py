n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
result = []
c = 0
max_len = max(len(n1), len(n2))
n1 = n1.zfill(max_len)
n2 = n2.zfill(max_len)
for i in range(max_len - 1, -1, -1):
    s = int(n1[i]) + int(n2[i]) + c
    result.append(str(s % 10))
    c = s // 10
    if c > 0:
        result.append(str(c))
result.reverse()
result_str = "".join(result)
print(f"Результат: {result_str}")
