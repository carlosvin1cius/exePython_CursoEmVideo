jogador = {}
gols = list()
jogador['Nome'] = str(input("Nome do Jogador: ")).capitalize()
npartidas = int(input(f"{jogador['Nome']}: Partidas disputadas: "))
jogador['Total'] = 0
for c in range(0, npartidas):
    gols.append(int(input(f"Gols na {c+1}° rodada: ")))
    jogador['Total'] += gols[c]
print('=-'*25)
jogador['Gols'] = gols
jogador['Média'] = jogador['Total']/npartidas
print(jogador)
print('=-'*25)

print(f'Jogador: {jogador["Nome"]}')
print(f'Gols marcados: {jogador["Gols"]}')
print(f'Média de gols por partida: {jogador["Média"]}')
print(f'Total de gols: {jogador["Total"]}')
print('=-'*25)
print(f"{jogador['Nome']} em {npartidas}: partidas")
for c, i in enumerate(gols):
    print(f'Partida {c+1}°: {i} gols marcados.')
