pessoas = list()
dados = dict()
midade = 0
while True:
    resp = " "
    dados.clear()
    dados['nome'] = str(input("Nome: ")).upper().strip()
    dados['sexo'] = str(input("Sexo: [m/f] ")).strip()[0]
    dados['idade'] = int(input("digite sua idade: "))
    midade += dados['idade']
    pessoas.append(dados.copy())
    while resp not in "SsNn":
        resp = str(input("Novo cadastro? [s/n]: ")).upper()[0]
    if resp in "Nn":
        print("Finalizado.")
        break
midade = midade/len(pessoas)
print("-="*25)
print(f"N° de cadastros: {len(pessoas)}")
print(f"Média de idade: {midade}")
print('Mulheres cadastradas: ', end='')
for p in pessoas:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]} ', end='')
print()
print("Pessoa acima da média: ", end='')
for p in pessoas:
    if p['idade'] > midade:
        print(f"{p['nome']}", end=',')
