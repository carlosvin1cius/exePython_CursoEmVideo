tabela = ("PALMEIRAS", "INTERNACIONAL", "FLUMINENSE", "FLAMENGO", "CORINTHIANS",
 "ATLHETICO-PR", "ATLETIGO-MG", "AMERICA-MG", "GOIÁS", "SÃO PAULO",
 "BOTAFOGO", "SANTOS", "BRAGANTINO", "FORTALEZA", "CEARÁ SC",
 "CORITIBA", "AVAI", "CUIABÁ", "ATLÉTICO-GO", "JUVENTUDE")
print(f"Lista de times: {tabela}")
print("=-"*60)
print(f"G-5: {tabela[0: 5]}")
print("=-"*60)
print(f"Z-4: {tabela[-4:]}")
print("=-"*60)
print(f"time em ordem alfabetica {sorted(tabela)}")
print("=-"*60)
print(f"Flamengo esta na {tabela.index('FLAMENGO')+1}° posição")

'''timeuser = str(input("DIGITE UM TIME PARA VER SUA POSIÇÃO NA TABELA: ")).upper()
for i in range(0, len(tabela)):
    if tabela[i] == timeuser:
        print(f"O {timeuser} esta na posição {i+1}")'''

