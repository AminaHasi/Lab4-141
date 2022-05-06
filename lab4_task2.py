# Лабораторна робота 4
# Гасимова Аміна
# 10. Дано рядки S, S1 і S2. Замінити в рядку S останнє входження рядка S1 на рядок S2
S = str(input("Введіть рядок S: "))
S1 = str(input("Введіть рядок S1: "))
S2 = str(input("Введіть рядок S2: "))
last_S1_find = S.rfind(S1)
last_S1_rep = S1.replace(S1, S2)
S = S + S1[:last_S1_find] + " " + last_S1_rep
print(S)
