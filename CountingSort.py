def countingSort(lista):
    tamanho = len(lista)
    saida = [0] * tamanho

    count = [0] * 10

    for i in range(0, tamanho):
        count[lista[i]] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = tamanho - 1
    while i >= 0:
        saida[count[lista[i]] - 1] = lista[i]
        count[lista[i]] -= 1
        i -= 1

    for i in range(0, tamanho):
        lista[i] = saida[i]

data = [4, 2, 2, 8, 3, 3, 1]
countingSort(data)
print("Resultado: ")
print(data)