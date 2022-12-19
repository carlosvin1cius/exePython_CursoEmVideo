statts = list()
jogadores = dict()
gols = list()
while True:
    gols.clear()
    jogadores.clear()
    jogadores["nome"] = str(input("Nome do Jogador: ")).capitalize().strip()
    jogadores['npartidas'] = int(input("N° Partidas: "))
    jogadores['Totalgols'] = 0
    for c in range (0, jogadores['npartidas']):
        gols.append(int(input(f"Gols: {c+1}° Rodada: ")))
        jogadores["Totalgols"] += gols[c]
    jogadores['gols'] = gols[:]
    statts.append(jogadores.copy())
    resp = " "
    while resp not in "SsNn":
        resp = str(input("CADASTRAR NOVO JOGADOR: [S/N] "))
    if resp in "Nn":
        print("-="*35)
        break

print(f"{'cod'} {'gols':>20} {'total':>20}")
print("-"*45)
for c, p in enumerate (statts):
        print(f"{c} {p['nome']:<17} {p['gols']} {p['Totalgols']:>15}")
while True:
    escolha = int(input("Digite o indice do jogador pra ver suas estatiscas: "))
    if escolha == 999:
        print("FINALIZADO")
        break
    if escolha >= len(statts):
        print("Numero invalido, digite um código valido de jogador cadastrado.")
        print("-"*45)
    else:
        for i, p in enumerate (statts):
            if i == escolha:
                print(f"{i} {p['nome']:<17} {p['gols']} {p['Totalgols']:>15}")
                print("-"*45)
print("-"*45)

