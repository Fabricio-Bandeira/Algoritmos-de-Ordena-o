def heap_sort(lista, n, i):
	maior_indice = i 
	esquerda = 2 * i + 1 
	direita = 2 * i + 2 

	if esquerda < n and lista[i] < lista[esquerda]:
		maior_indice = esquerda

	if direita < n and lista[maior_indice] < lista[direita]:
		maior_indice = direita

	if maior_indice != i:
		(lista[i], lista[maior_indice]) = (lista[maior_indice], lista[i]) 

		heap_sort(lista, n, maior_indice)

def heapSort(lista):
	n = len(lista)

	for i in range(n // 2, -1, -1):
		heap_sort(lista, n, i)

	for i in range(n - 1, 0, -1):
		(lista[i], lista[0]) = (lista[0], lista[i]) 
		heap_sort(lista, i, 0)

lista = [12, 11, 13, 5, 1, 4, 9, 6, 7, ]
heapSort(lista)
n = len(lista)
lista_ordenada = []

print('Resultado da ordenação: ')
for i in range(n):
	lista_ordenada.append(lista[i])
	
print(lista_ordenada)

