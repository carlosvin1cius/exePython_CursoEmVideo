print("===== EXERCICIO 062 =====")
ntermo = int(input("DIGITE O TERMO: "))
pa = int(input("DIGITE O TERMO DE PROGRESSÃO: "))
c = 0
termodesejados = 10
while c < termodesejados:
    ntermo = ntermo + pa
    print("{}".format(ntermo), end= " -> ")
    if c+1 == termodesejados:
        r = int(input("DESEJA CONTINUAR E MOSTRAS MAIS TERMOS: [0 PRA NÃO] "))
        termodesejados += r
        if r == 0:
            print("FIM")
    c += 1