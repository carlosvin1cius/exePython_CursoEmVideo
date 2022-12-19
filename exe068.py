print("===== EXERCICIO 069 =====")
from random import randrange
resultado = pts = 0
while True:
    valor = int(input("DIGITE UM VALOR: "))
    pcn = randrange(1, 11)
    resultado = valor + pcn
    escolha = str(input("PAR OU IMPAR? [P/I] ")).strip().upper()
    print (f"{pcn} Foi escolhido pelo pc.")
    print("-"*20)
    if escolha in "PI":
        if resultado % 2 == 0:
            print(f"VOCE JOGOU {valor} E O COMPUTADOR {pcn}. TOTAL {resultado} = PAR")
            resultado = "PAR"
        else:
            print(f"VOCE JOGOU {valor} E O COMPUTADOR {pcn}. TOTAL {resultado} = IMPAR")
            resultado = "IMPAR"
            
        if escolha == "P" and resultado == "PAR":
            print ("VOCÊ VENCEU!")
            pts += 1
        elif escolha == "I" and resultado == "IMPAR":
            print("VOCE VENCEU!")
            pts += 1
        else:
            print("VOCE PERDEU!")
            break
        print("-"*20)
        print("VAMOS JOGAR NOVAMENTE...")
        print("-"*20)
    else:
        print("escolha não é valida. tente novamente...")
print("=-"*10)
print(f"GAME OVER! O jogador venceu {pts} VEZES")
