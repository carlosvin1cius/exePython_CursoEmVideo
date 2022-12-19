from datetime import date
data = date.today().year
hora = date.today().timetuple
maioridade = 0
menoridade = 0
print(hora)
for c in range (1, 8):
    idade = int(input("DIGITE O ANO DE NASCIMENTO DA {}° PESSOA: ".format(c)))
    if data - idade >= 18:
        maioridade = maioridade + 1
    else:
        menoridade = menoridade + 1
print("O numero de pessoas maiores de 18 anos na lista é de {}\nO numero de menores de idade na lista é de {}".format(maioridade, menoridade))
