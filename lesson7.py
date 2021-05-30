
# exercise 1
for i in range(26):
    print("Hello, GloAcademy!")

# exercise 2
ex2_max = int(input())
for i in range(ex2_max):
    print(f"Квадрат числа {i} равен {i**2}")
    if i == ex2_max:
        print(f"Квадрат числа {i+1} равен {(i+1)**2}")

# exercise 3
ex3_min = int(input())
ex3_max = int(input())
for i in range(ex3_min, ex3_max + 1):
    print(i)

# exercise 4
ex4_min = int(input())
ex4_max = int(input())
for i in range(ex4_min, ex4_max + 1):
    print(i)


# exercise 5
ex5_num = int(input())
for i in range(1, 11):
    print(f"{ex5_num} x {i} = {ex5_num * i}")

# exercise 6
ex6_num = int(input())
ex6_sum = 0

for i in range(1, ex6_num + 1):
    if i % 10 == 1 or i % 10 == 3 or i % 10 == 7:
        ex6_sum = ex6_sum + i

print(ex6_sum)

# exercise 7
ex7_num = int(input())
ex7_sum = 1
for i in range(1, ex7_num + 1):
    if i % 10 == 2 or i % 10 == 9:
        ex7_sum = ex7_sum * i

if ex7_sum == 1:
    print(0)
else:
    print(ex7_sum)

# exercise 8
print("Введите минимальное число")
ex8_num_min = int(input())
print("Введите максимальное число")
ex8_num_max = int(input())
print("Введите кол-во цифр для ввода далее")
ex8_num = int(input())
if ex8_num >= 2:
    for i in range(1, ex8_num + 1):
        print("____________________________________")
        number = int(input())
        if number < ex8_num_min:
            ex8_num_min = number
        if number > ex8_num_max:
            ex8_num_max = number

    print(f"Минимум равен {ex8_num_min}")
    print(f"Максимум равен {ex8_num_max}")

# exercise 9
flag = 0
print("Введите кол-во цифр для ввода далее")
ex9_num = int(input())

for i in range(1, ex9_num + 1):
    print("____________________________________")
    num = int(input())
    if num % 10 != 2:
        flag = 1
if flag == 1:
    print("YES")
else:
    print("NO")

# exercise 10
flag = 0
print("Введите кол-во цифр для ввода далее")
ex10_num = int(input())
for i in range(1, ex10_num + 1):
    print("____________________________________")
    num = int(input())
    if num % 10 != 2:
        flag += 1
if flag == ex10_num:
    print("YES")
else:
    print("NO")

