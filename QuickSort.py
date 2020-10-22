import time
inicio = time.time()

def partition(arr, low, high):
    i = (low-1)         
    pivot = arr[high]     
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
 
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return (i+1)

 
 
def quickSort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi-1)
        quickSort(arr, pi+1, high)
 
 
from random import sample

random = sample(range(0, 1500), 1500)
crescente = sorted(random)
decrescente = sorted(random, reverse=True)
print(crescente)

arr = random
n = len(arr)
quickSort(arr,0,n-1)
print(arr)

fim = time.time()
diferenca = fim - inicio
print(f'{diferenca:.5f}s')



 

