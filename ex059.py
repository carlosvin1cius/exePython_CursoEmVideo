print("===== EXERCICIO 059 =====")
n1 = int(input("DIGITE UM NUMERO: "))
n2 = int(input("DIGITE UM NOVO NUMERO: "))
escolha = 0
while escolha != 5:
    escolha = int(input('''===========
[1] SOMAR
[2]MULTIPLICAR
[3]MAIOR
[4]NOVOS NÚMEROS
[5]SAIR DO PROGRAMA
SUA ESCOLHA: '''))
    if escolha == 1:
        s = n1 + n2
        print("A soma é: {}".format(s))
    elif escolha == 2:
        m = n1 * n2
        print("A multiplicação é: {}".format(m))
    elif escolha == 3:
        if n1 > n2:
            print("{} é maior".format(n1))
        elif n2 > n1:
            print("{} é maior".format(n2))
        else:
            print("{} e {} são iguais".format(n1, n2))
    elif escolha == 4:
        n1 = int(input("DIGITE UM NOVO NUMERO: "))
        n2 = int(input("DIIGTE UM SEGUNDO NOVO NUMERO: "))
    elif escolha == 5:
        print ("Fim")
    else:
        print("OPÇÃO INVALIDA.")
