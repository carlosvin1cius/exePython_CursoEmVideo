def area(a, b):
    ar = a*b
    print(f"A área de um terreno {a}x{b} é de {ar}m²")
    
area(a = float(input("DIGITE A LARGURA: ")), 
    b= float(input("DIGITE A ALTURA: ")))
print(area)