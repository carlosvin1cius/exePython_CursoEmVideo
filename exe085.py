nums = [[], []]
for i in range(0, 7):
    valor = int(input(f"DIGITE O {i+1}° VALOR: "))
    if valor %2 == 0:
        nums[0].append(valor)
    else:
        nums[1].append(valor)
print("=-"*30)
nums[0].sort()
nums[1].sort()
print(f"VALORES DIGITADOS: {nums}")
print(f"VALORES IMPARES {nums[0]}")
print(f"VALORES PARES: {nums[1]}")