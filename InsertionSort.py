def insertion_sort(lista):
    for i in range(1, len(lista)):
        valor = lista[i]

        while lista[i-1] > valor and i > 0:
            lista[i-1], lista[i] = lista[i], lista[i-1]
            i -= 1
    return lista

lista = [3, 2, 5, 7, 4]

print(insertion_sort(lista))