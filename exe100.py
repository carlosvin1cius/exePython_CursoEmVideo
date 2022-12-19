from random import randint
numeros = list()

def sorteia(lista):
    for i in range(0, 5):
        lista.append(randint(1, 10))   
    print(f"lista de numeros: {lista}")
def somaPar(lista):
    spares = 0
    for i in lista:
        if i % 2 == 0:
            spares += i
    print(f"soma de pares: {spares}")
sorteia(numeros)
somaPar(numeros)
