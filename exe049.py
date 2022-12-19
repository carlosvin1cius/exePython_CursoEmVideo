print("===== EXERCICIO 049 =====")
tabuada =  int(input("DIGITE A TABUADA DESEJADA: "))
result = 0
for c in range (1, 11):
    result = tabuada*c
    print("{} X {} = {}".format(tabuada, c, result))
