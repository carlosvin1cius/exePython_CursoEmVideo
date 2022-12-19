def maior(* nums):
    cont = maior = 0
    for i in nums:
        print(f"{i} ", end=" ", flush=True)
        if cont == 0:
            maior = i
        elif i > maior: 
            maior = i
        cont += 1
    print(f"N° Valores informados: {cont}")
    print(f"Maior valor: {maior}")
maior(9, 8, 5, 10, 15, 17)
maior(9, 15, 18, 1)
