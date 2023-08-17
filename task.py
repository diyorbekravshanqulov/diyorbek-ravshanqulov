import os
os.system("cls")

# 1
num1 = list(map(int, input("Enter first list: ").split()))
num2 = list(map(int, input("Enter second list: ").split()))
for i in num2:
    num1.append(i)
num1.sort()
print(num1)

2
num = list(map(int, input("Enter list: ").split()))
n, m, temp = 0, 0, 0
for i in num:
    for j in num:
        if i == j:
            n+=1
    if m < n:
        m, temp = n, i
    else:
        continue
print(temp)

# # 3
def func(num):
    ttl = list()
    for i in range(1, len(num) - 1, 2):
        ttl.append(num[i] + num[i + 1])
    if max(ttl) % 2 == 0:
        return max(ttl)
    else:
        return -1

num = list(map(int, input("Enter list: ").split()))
print(func(num))

# 4
lst = list(map(str, input("Enter list: ").split()))
n = input("Nima bilan ajratilishini kiriting: ")
temp = list()
for i in lst:
    temp.append(i.split(n))
print(temp)