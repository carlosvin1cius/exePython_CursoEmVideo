matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = sfirstcol = ssegl = pos = cpos = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"DIGITE O VALOR: [{l, c}]: "))

print("=*"*30)
print(f"A soma dos valores pares é: {soma}")
print(f"A soma da terceira coluna é {sfirstcol}")
print(f"A soma da segunda linha é {ssegl}")

#*** renicializando os contadores presentes no print