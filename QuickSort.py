import time

def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista.pop()

    elementos_max = []
    elementos_min = []

    for elemento in lista:
        if elemento > pivot:
            elementos_max.append(elemento)
        else:
            elementos_min.append(elemento)
    return quick_sort(elementos_min) + [pivot] + quick_sort(elementos_max)


print(quick_sort([4,2,7,4,1,0,5,7,3]))


