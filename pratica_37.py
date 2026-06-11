#Função que usa o Insertion Sort para ordenar uma lista de números inteiros
def insertion_sort(lista):
    for i in range(1, len(lista)): #Começa uma varredura da lista a partir do segundo elemento
        chave = lista[i] #Guarda o valor do segundo elemento na variável chave
        j = i - 1 #Evidencia o índice do primeiro elemento
        while j >= 0 and lista[j] > chave: #Começa um loop se o primeiro elemento (com índice j >= 0) for maior que o segundo
            lista[j + 1] = lista[j] #O valor do segundo elemento "vira" o valor do primeiro
            j = j - 1 #Evidencia o índice do primeiro elemento da lista (a restrição j >= 0 age aqui!)
        lista[j + 1] = chave #O loop fez com que j = -1. Daí, note que lista[j + 1] = chave é a mesma coisa que lista[0] = chave
    return lista

lista = [14, 77, 18, -4, 56, 4, 0, 9, -8, 100]
print(insertion_sort(lista))