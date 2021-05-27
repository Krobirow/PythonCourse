
# exercise 1
ex1_num1 = input()
print(len(ex1_num1))

# exercise 2
ex2_str1 = input()

if "Glo Academy" in ex2_str1:
    print("YES")
else:
    print("NO")

# exercise 3
ex3_list1 = [input(), input(), input()]
print(max(ex3_list1, key=len))

# exercise 4
ex4_str1 = input()
print(ex4_str1 * 5)

# exercise 5
ex5_str1 = input()

if "@" and "." in ex5_str1:
    print("Корректный")
else:
    print("Некорректный")
