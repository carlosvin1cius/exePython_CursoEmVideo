print("===== EXERCICIO 070 =====")
s = maismil = menorv = c = 0
menorn = " "
while True:
    nprod = str(input("Nome Produto: ")).strip().title()
    valor = float(input("Valor produto: R$"))
    s += valor
    if valor > 1000:
        maismil += 1
    if c == 0 or nprod < menorv:
        menorn = nprod
        menorv = valor
    r = " "
    c += 1
    while r not in "SN":
        r = str(input("Quer Continuar? [S/N] ")).strip().upper()[0]
    if r == "N":
        print("---------- FIM DO PROGRAMA ----------")
        break
print(f"VALOR TOTAL: {s}")
print(f"{maismil} CUSTAM MAIS QUE R$1,0000.")
print(f"{menorn} é o produto mais barato. VALOR: R${menorv}")
