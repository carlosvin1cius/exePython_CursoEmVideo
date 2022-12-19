print("===== EXERCICIO 042 =====")
r1 = int(input("Digite a medida da primeira reta: "))
r2 = int(input("Digite a medida da segunda reta: "))
r3 = int(input("Digite a medida da terceira reta: "))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("As medidas {}, {}, {} são capazes de formar um triangulo.".format(r1, r2, r3))
    if r1 == r2 == r3:
        print("O triangulo é EQUILATERO!")
    elif r1 == r2 or r2 == r3 or r3 == r1:
        print("O triangulo é ISÓSCELES!")
    else:
        print("O triangulo é ESCALENO!")
else:
    print("As medidas {}, {}, {} não formam um triangulo.".format(r1, r2, r3))