print("===== EXERCICIO 028 =====")
import random
from time import sleep
npc = random.randint(0, 5) # sorteio do computador
nuser = int(input("O computador pensou em um numero. Digite você um numero entre 0 e 5: ")) # numero do jogador
print("PROCESSANDO...")
sleep(2.5)
if npc == nuser:
    print("O COMPUTADOR CHUTOU O NUMERO {} E VOCÊ DIGITOU {}. PARABENS VOCÊ CHUTOU O MESMO NUMERO DO COMPUTADOR!".format(npc, nuser))
else:
    print("O COMPUTADOR CHUTOU O NUMERO {} E VOCÊ DIGITOU {}. O numero digitado não é o mesmo!".format(npc, nuser))
