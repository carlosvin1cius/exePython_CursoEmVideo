print("===== EXERCICIO 037 =====")
numero = int(input("DIGITE UM NUMERO INTEIRO: "))
print("="*25)
escolha = int(input('''ESCOLHA UMA OPÇÃO DE CONVERÇÃO:
[1]BINARIO
[2]OCTAL
[3]HEXADECIMAL
SUA OPÇÃO: '''))
print("="*25)
if escolha == 1:
    print("{} CONVERTIDO PARA BINARIO É {}".format(numero, bin(numero)))
elif escolha == 2:
    print("{} CONVERTIDO PARA OCTAL É {}".format(numero, oct(numero)))
elif escolha == 3:
    print("{} CONVERTIDO PARA HEXADECIMAL É {}".format(numero, hex(numero)))
else:
    print("OPÇÃO ESCOLHIDA INVALIDA!")
