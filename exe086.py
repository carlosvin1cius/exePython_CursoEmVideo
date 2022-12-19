matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"DIGITE O VALOR: "))
print("=*"*30)
for i in matriz:        
    print(f"[ {i[0]} ][ {i[1]} ][ {i[2]} ]")
