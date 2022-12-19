print("===== EXERCICIO 056 =====")
mage = 0
contF = 0
for c in range (1, 4):
    print("----- {}° PESSOA -----".format(c))
    nome = str(input("Nome: "))
    age = int(input("Idade: "))
    mage = mage + age
    sexo = str(input("Sexo [M/F]: "))
    if sexo in "Ff" and age < 20:
        contF = contF+1
    if c == 1:
        maisvelho = nome
        maisage = age
    elif maisage < age and sexo in "Mm":
        maisvelho = nome
        maisage = age
mediaage = mage/c
print("A média de idade do grupo é de {}".format(mediaage))
print("O homem mais velho é {} e ele tem {} anos.".format(maisvelho, maisage))
print("{} mulheres tem menos de 20 anos".format(contF))
