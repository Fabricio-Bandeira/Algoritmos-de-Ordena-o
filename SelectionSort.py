def selection_sort(lista):
    for i in range(len(lista)-1):
        minimo = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[minimo]:
                minimo = j
        if minimo != i:
            lista[minimo], lista[i] = lista[i], lista[minimo]
    return lista

print(selection_sort([14,4,1,76,58,25,9,4]))
