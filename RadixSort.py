def ordenacao_por_contagem(lista, exp):
    n = len(lista)
    saida = [0] * n
    contagem = [0] * 10
    for i in range(n):
        indice = (lista[i] // exp) % 10
        contagem[indice] += 1
    for i in range(1, 10):
        contagem[i] += contagem[i - 1]
    i = n - 1
    while i >= 0:
        indice = (lista[i] // exp) % 10
        saida[contagem[indice] - 1] = lista[i]
        contagem[indice] -= 1
        i -= 1
    for i in range(n):
        lista[i] = saida[i]
def radix_sort(lista):
    max_num = max(lista)
    exp = 1
    while max_num // exp > 0:
        ordenacao_por_contagem(lista, exp)
        exp *= 10
lista = [170, 45, 75, 90, 802, 24, 2, 66]
print("lista original:", lista)

radix_sort(lista)
print("lista ordenado:", lista)
