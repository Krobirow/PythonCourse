from math import ceil
# exercise 1
ex1_num = 24
count = 0
while ex1_num % 2 == 0:
    ex1_num = ex1_num // 2
    count += 1
print(count)

# exercise 2
ex2_num = int(input())
total = 0
while ex2_num != 0:
    last_digit = ex2_num % 10
    if last_digit == 5:
        total += 1

    ex2_num = ex2_num // 10

print(total)

# exercise 3
ex3_num = 1
num = ex3_num
total = 0
while num != 0:
    total += num % 10
    num = num // 10

    if ex3_num % total == 0:
        print("YES")
    else:
        print("NO")

# exercise 4
ex4_num = 3841234510
ex4_max = 1
ex4_min = 1

while ex4_num >= 10:
    last_digit = ex4_num % 10
    ex4_num = ex4_num // 10

    if last_digit > ex4_max:
        ex4_max = last_digit
    if last_digit < ex4_min:
        ex4_min = last_digit

print(f"Максимальная цифра равна {ex4_max}")
print(f"Минимальная цифра равна {ex4_min}")

# exercise 5
ex5_num = int(input())
positive = 0
negative = 0

while ex5_num != 0:
    ex5_num = int(input())
    if ex5_num > 0:
        positive += 1
    elif ex5_num < 0:
        negative += 1

print(positive * negative)

# exercise 6
ex6_num = int(input())
ex6_sum = 0
count = 0

while ex6_num != 0:
    ex6_num = int(input())
    count += 1
    ex6_sum += ex6_num

print(ceil(ex6_sum / count))
