def bucketSort(lista):
    bucket = []

    for i in range(len(lista)):
        bucket.append([])

    for j in lista:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    for i in range(len(lista)):
        bucket[i] = sorted(bucket[i])

    k = 0
    for i in range(len(lista)):
        for j in range(len(bucket[i])):
            lista[k] = bucket[i][j]
            k += 1
    return lista


array = [0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51]
print("Resultado: ")
print(bucketSort(array))