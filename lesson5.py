from math import ceil

# exercise 1
ex1_num1 = input()
ex1_num2 = input()

if ex1_num1 == ex1_num2:
    print("Все окей!")
else:
    print("Пароли не совпадают!")

# exercise 2
ex2_num1 = float(input())

if ex2_num1 > 0:
    print("Положительное")
else:
    if ex2_num1 < 0:
        print("Отрицательное")
    else:
        print("Ноль")

# exercise 3
ex3_num1 = int(input())

sum1 = (ex3_num1 // 100000) + (ex3_num1 // 10000 % 10) + (ex3_num1 // 1000 % 10)
sum2 = (ex3_num1 % 10) + (ex3_num1 % 100 // 10) + (ex3_num1 % 1000 // 100)

if len(str(ex3_num1)) == 6:
    print(len(str(ex3_num1)))
    if sum1 == sum2:
        print(f"Билт {ex3_num1} счастливый")
    else:
        print(f"Билет {ex3_num1} НЕсчастливый")
else:
    print("Число не из 6 цифр!")

# exercise 4
w = int(input())

if 1 < w < 100:
    if w > 2 and w % 2 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("Вес дыни должен быть более 1 кг и менее 100 кг")

# exercise 5
k = int(input())
m = int(input())
print(ceil(k / m))

# exercise 6
pocket = int(input())

if 0 <= pocket <= 36:
    if pocket == 0:
        print(f"карман {pocket} зеленый")
    elif pocket % 2 == 0:
        if 19 <= pocket <= 28 or 0 < pocket <= 10:
            print(f"карман {pocket} четный черный")
        elif 29 <= pocket <= 36 or 11 <= pocket <= 18:
            print(f"карман {pocket} четный красный")
    elif pocket % 2 != 0:
        if 19 <= pocket <= 28 or 0 < pocket <= 10:
            print(f"карман {pocket} нечетный красный")
        elif 29 <= pocket <= 36 or 11 <= pocket <= 18:
            print(f"карман {pocket} нечетный черный")
else:
    print("Ошибка ввода! Ведено число вне диапазона 0 - 36")
