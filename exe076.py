preços = ("LÁPIS", 1.75, "Borracha", 2.00, "Caderno", 15.90, "Estojo", 25.00, "Transferidor", 4.20, 
          "Compasso", 9.99, "Mochila", 120.32, "Canetas", 22.30, "Livro", 34.90)
prox = 1
print("-"*39)
print(f"LISTAGEM DE PREÇOS")
print("-"*39)
for i in range(0, len(preços), 2):
        print(f"{preços[i]:30}R$ {preços[prox]:6}")
        prox += 2
print("-"*39)
