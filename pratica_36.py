#Função que usa o Bubble Sort para ordenar uma lista de números inteiros
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

lista = [5, 3, 2, 1, 90, 6]
print(bubble_sort(lista))