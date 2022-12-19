from sqlite3 import Date
pessoa = {}
ano = Date.today().year
pessoa['Nome'] = str(input("NOME COMPLETO: ")).upper()
pessoa['Idade'] = (ano - int(input("DIGITE O ANO DE NASCIMENTO: ")))
pessoa['Ctps'] = int(input("N° CARTEIRA DE TRABALHO: "))
if pessoa['Ctps'] != 0:
    pessoa['Adm'] = int(input("ANO CONTRATAÇÃO: "))
    pessoa['Salario'] = float(input("SALARIO: R$ "))
    pessoa['Idade de aposentadoria: '] = 35 - (ano - pessoa['Adm']) + pessoa['Idade']
else:
    print(f'{pessoa["Nome"]} não tem carteira de trabalho.')
for k, v in pessoa.items():
    print(f'{k}: {v}')