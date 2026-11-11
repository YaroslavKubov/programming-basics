
n = int(input("Введіть додатне число n: "))

total = 0

print("Числа від 1 до n:")

for i in range(1, n + 1):
    print(i)
    total += i

print("Сума:", total)

current = n

print("Зворотний відлік:")

while current >= 1:
    print(current)
    current -= 1
