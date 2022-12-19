maiorp = 0
menorp = 0
for c in range(1, 6):
    peso = float(input("PESO DA {}° PESSOA: ".format(c)))
    if c == 1:
        maiorp = peso
        menorp = peso
    elif peso > maiorp:
        maiorp = peso
    if peso <= menorp:
            menorp = peso
print("MAIOR PESO REGISTRADDO: {}kg\nMENOR PESO REGISTRADO: {}kg".format(maiorp, menorp))
