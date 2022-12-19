ext = ("ZERO", "UM", "DOIS", "TRÊS", "QUATRO", "CINCO", "SEIS", "SETE", "OITO", "NOVE", "DEZ", "ONZE", "DOZE", "TREZE", "QUATORZE", "QUINZE", "DEZESSEIS", "DEZESETE", "DEZOITO", "DEZENOVE", "VINTE")
while True:
    escolha = int(input("Digite um numero para velo por extenso [1 a 20]: "))
    resp = " "
    if 0 <= escolha <= 20:
        print(f"{escolha} por extenso: {ext[escolha]}")
        while resp not in "SN":
            resp = str(input("Deseja verificar outro numero [S/N] ")).strip().upper()[0]
        if resp == "N":
            print("Finalizado.")
            break
    else:
        print("Numero invalido, tente novamente.", end= " ")
    
