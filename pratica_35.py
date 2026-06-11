#Função que usa o Selection Sort para ordenar uma lista de números inteiros
def selection_sort(lista):
    n = len(lista)
    for i in range(n):
        indice_do_menor = i
        for j in range(i + 1, n):
            if lista[j] < lista[indice_do_menor]:
                indice_do_menor = j
        if i != indice_do_menor: lista[i], lista[indice_do_menor] = lista[indice_do_menor], lista[i]
    return lista

lista = [14, 7, 8, 34, 56, 4, 0, 9, -8, 100]
print(selection_sort(lista))