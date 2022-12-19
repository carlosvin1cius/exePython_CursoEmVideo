print("===== EXERCICIO 041 =====")
from datetime import date
nome = str(input("DIGITE SEU NOME: ")).upper()
anonasc = int(input("OLÁ, {} DIGITE O ANO DO SEU NASCIMENTO: ".format(nome)))
anoatual = date.today().year
idade = anoatual - anonasc
if idade <= 9:
    print("{} você tem {} e é classificado atualmente como: MIRIM".format(nome, idade))
elif idade <= 14:
    print("{} você tem {} e é classificado atualmente como: INFANTIL".format(nome, idade))
elif idade <= 19:
    print("{} você tem {} e é classificado atualmente como: JUNIOR".format(nome, idade))
elif idade <= 25:
    print("{} você tem {} e é classificado atualmente como: SENIOR".format(nome, idade))
else:
    print("{} você tem {} e é classificado atualmente como: MASTER".format(nome, idade))
