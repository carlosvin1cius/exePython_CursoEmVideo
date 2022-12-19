print("===== EXERCICIO 067 =====")
n = s = c = 0
while True:
    n = int(input("DIGITE UM NUMERO: [999] para o programa "))
    if n == 999:
        break
    s += n
    c += 1
print(f"A soma dos {c} numeros digitados é {s}")
