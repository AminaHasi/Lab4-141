# Лабораторна робота 4
# Гасимова Аміна
# 15. У списку чисел перевірити, чи всі елементи є унікальними, тобто кожне число зустрічається
# тільки один раз.
from random import random

N = 10
li = [0] * N
for i in range(N):
    li[i] = int(random() * 50)
print(li)

for i in range(N-1):
    for j in range(i+1, N):
        if li[i] == li[j]:
            print("Є одинакові числа")
            quit()
print("Всі числа різні")
