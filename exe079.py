print("===== EXERCICIO 079 =====")
n = list()
while True:
    res = ""
    num = int(input("DIGITE UM VALOR: "))
    if num in n:
        print("JA tem esse numero na lista. Valor não insirido")
    else:
        n.append(num)
        res = str(input("QUER CONTINUAR?: ")).strip().upper()[0]
        if res in "N":
            break
n.sort()
print(n)
