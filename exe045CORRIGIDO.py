print("==== EXERCICIO 045 =====")
from random import randint
from time import sleep
itens = ("PEDRA", "PAPEL", "TESOURA")
escolhapc = randint(0, 2)
escolha = int(input('''OPÇÕES:
[0] PEDRA
[1] PAPEL
[2] TESOURA
DIGITE SUA JOGADA: '''))
print("="*25)
if 2 >= escolha >=0:
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PÔ")
    print("=" * 25)
    print("ESCOLHA JOGADOR: {} \nESCOLHA COMPUTADOR: {}".format(itens[escolha], itens[escolhapc]))
    if escolha != escolhapc:
        if escolha == 0 and escolhapc == 2:
            vencedor = "JOGADOR"
        elif escolha == 1 and escolhapc == 0:
            vencedor = "JOGADOR"
        elif escolha == 2 and escolhapc == 1:
            vencedor = "JOGADOR"
        else:
            vencedor = "COMPUTADOR"
        print("{} VENCEU".format(vencedor))
    else:
        print("EMPATE")
else:
    print("OPÇÃO INVALIDA")
