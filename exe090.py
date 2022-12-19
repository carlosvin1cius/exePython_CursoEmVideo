aluno = {}
aluno['nome'] = str(input("NOME: ")).upper()
aluno['Média'] = int(input("MÉDIA DO SEMESTRE: "))
if aluno['Média'] >= 7:
    aluno['situação'] = 'APROVADO'
else:
    aluno['situação'] = 'REPROVADO'
print("-="*30)
print(f'Nome: {aluno["nome"]}')
print(f'Média: {aluno["Média"]}')
print(f'Situação: {aluno["situação"]}')
