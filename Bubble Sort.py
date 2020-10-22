import time
inicio = time.time()

def bubble_sort(lista):
    elementos = len(lista)-1
    ordenado = False
    while not ordenado:
        ordenado = True
        for i in range(elementos):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1],lista[i]
                ordenado = False        
              
    return lista

from random import sample
random = sample(range(0, 1500), 1500)
crescente = sorted(random)
decrescente = sorted(random, reverse=True)


lista = random
bubble_sort(lista)
print(lista)

fim = time.time()
diferenca = fim - inicio
print(f'{diferenca:.5f}s')
