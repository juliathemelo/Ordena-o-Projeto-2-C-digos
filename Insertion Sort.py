import time
inicio = time.time()
def insertionSort(arr): 
    for i in range(1, len(arr)): 
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
  
from random import sample

random = sample(range(0, 8500), 8500)  
crescente = sorted(random)
decrescente = sorted(random, reverse=True)

arr = [3,8,2,10,4]
insertionSort(arr)
print(arr)

fim = time.time()
diferenca = fim - inicio
#print(f'{diferenca:.5f}s')
