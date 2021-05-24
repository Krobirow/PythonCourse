from math import floor

# exercise 1
ex1_num1 = int(input())
ex1_num2 = int(input())

print((ex1_num1 ** 2) + (ex1_num2 ** 2))

# exercise 2
ex2_num1 = int(input())
ex2_num2 = int(input())
# 1
print(ex2_num1, "умноженное на", ex2_num2, "равно", ex2_num1 * ex2_num2)
# 2
print(ex2_num1, "деленное на", ex2_num2, "равно", float(ex2_num1 / ex2_num2))
# 3
print(ex2_num1, "нацело деленное на", ex2_num2, "равно", ex2_num1 // ex2_num2)
# 4
print("Остаток от деления", ex2_num1, "на", ex2_num2, "равно", ex2_num1 % ex2_num2)
# 5
print(ex2_num1, "в степени", ex2_num2, "равно", ex2_num1 ** ex2_num2)

# exercise 3
ex3_num1 = int(input())
# 1
print("Сумма цифр числа", ex3_num1, "равна", int((ex3_num1 % 10) + (ex3_num1 % 100 // 10) + (ex3_num1 // 100)))
# 2
print("Произведение цифр числа", ex3_num1, "равна", int((ex3_num1 % 10) * (ex3_num1 % 100 // 10) * (ex3_num1 // 100)))

# exercise 4
r = int(input())
k = int(input())
n = int(input())

coins_total_amount = (r * n * 100) + (k * n)

print("За", n, "мяча нужно заплатить", int((coins_total_amount - (coins_total_amount % 100)) / 100), "рублей и",
      (coins_total_amount % 100), "копеек")

# exercise 5
timeRemaining = int(input())

second = floor(timeRemaining % 60)
minutes = floor((timeRemaining / 60) % 60)
hours = floor(timeRemaining / 3600)

print(f"{timeRemaining} секунд - это {hours} час {minutes} минут {second} секунд")

# exercise 6
ex6_num1 = 9045
print(max(ex6_num1 % 10, ex6_num1 % 100 // 10, ex6_num1 // 100 % 10, ex6_num1 // 1000))

# exercise 7
ex7_num1 = int(input())
print(f"У числа {ex7_num1} сумма последних трех цифр равна"
      f" {ex7_num1 % 1000 // 100 + ex7_num1 % 100 // 10 + ex7_num1 % 10}")
