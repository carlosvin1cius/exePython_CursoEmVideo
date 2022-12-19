def contador(ini, fim, passo):
    print(f"Contagem de {ini} até {fim} de {passo} em {passo}:")
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo = 1  
    if ini < fim:
        cont = ini
        while cont <= fim:
            print(f"{cont}", end=" ")
            cont += passo
        print("FIM")
        print("-"*30)
    if ini > fim:
        cont = ini
        while cont >= fim:
            print(f"{cont}", end=" ")
            cont -= passo
        print("FIM")
        print("-"*30)
        
contador(1, 10, 1)
contador(10, 0, 2)
contador(ini = int(input("DIGITE O INICIO: ")),
          fim = int(input("FIM: ")),
          passo = int (input("PASSO: ")))
