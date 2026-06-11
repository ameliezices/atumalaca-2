#Função que usa o Insertion Sort para ordenar uma lista de números inteiros
def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j = j - 1
        lista[j + 1] = chave
    return lista

lista = [14, 77, 18, -4, 56, 4, 0, 9, -8, 100]
print(insertion_sort(lista))