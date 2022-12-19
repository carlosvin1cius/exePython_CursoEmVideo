print("===== EXERCICIO 065 =====")
n = maior = menor = count = s = 0
r = "S"
while r == "S":
    n = int(input("DIGITE UM NUMERO: "))
    s += n
    count += 1
    if count == 1:
        maior = menor = n
    elif maior < n:
        maior = n
    elif menor > n:
        menor = n
    r = str(input("quer continuar: [S/N] ")).strip().upper()
print("A média dos numeros digitados foi: {}".format(s/count))
print("O maior numero é {}, o menor é {}".format(maior, menor))
print("FINALIZADO.")
