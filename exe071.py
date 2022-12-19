print("===== EXERCICIO 070 =====")
valor = int(input("VALOR A SER SACADO: R$"))
t50 = t20 = t10 = t1 = s = 0
while True:
    while valor >= 50:
        t50 += 1
        valor -= 50
    if valor < 50 and valor >= 20:
        t20 += 1
        valor -= 20
    if valor < 20 and valor >= 10:
        t10 += 1
        valor -= 10
    if valor < 10 and valor >= 1:
        t1 += 1
        valor -= 1
    if valor == 0:
        print("finalizado")
        break
if t50 >= 1:
    print(f"{t50} Cédulas de R$50.")
if t20 >= 1:
    print(f"{t20} Cédulas de R$20.")
if t10 >= 1:
    print(f"{t10} Cédulas de R$10.")
if t1 >=1:
    print(f"{t1} Cédulas de R$1")
