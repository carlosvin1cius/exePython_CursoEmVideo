print("===== EXERCICIO 052 =====")
n = int(input("DIGITE UM NUMERO: "))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
    print(c)
print("O {} foi divisel {} vezes".format(n, tot))