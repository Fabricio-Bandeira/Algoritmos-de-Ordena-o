# Merge Sort
# Ele separa o problema principal em subproblemas para resolver um de cada vez.
# Basicamente, ele divide a lista em várias sublistas até que todas as listas fiquem com 
# somente 1 elemento. 

def merge_sort(lista):
    if len(lista) > 1:
        metade = len(lista) // 2

        metade1 = lista[:metade]
        metade2 = lista[metade:]

        merge_sort(metade1)
        merge_sort(metade2)

        i = j = k = 0

        while i < len(metade1) and j < len(metade2):
            if metade1[i] < metade2[j]:
                lista[k] = metade1[i]
                i += 1
            else:
                lista[k] = metade2[j]
                j += 1
            k += 1

        while i < len(metade1):
            lista[k] = metade1[i]
            i += 1
            k += 1

        while j < len(metade2):
            lista[k] = metade2[j]
            j += 1
            k += 1

lista = [12, 11, 13, 5, 6, 7]
merge_sort(lista)
print("Lista ordenada é:", lista)