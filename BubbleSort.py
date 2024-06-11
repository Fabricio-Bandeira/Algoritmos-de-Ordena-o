def bubble_sort(lista):
    tamanho = len(lista) - 1
    ordenada = False
    while ordenada == False:
        ordenada = True
        for i in range(tamanho):
            if lista[i] > lista[i+1]:
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenada = False
    return lista


numeros = [2, 1, 7, 5, 3] 
print(bubble_sort(numeros))
