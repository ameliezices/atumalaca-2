#Refazer as funções busca sequencial e busca binária assumindo que a lista possui chaves que podem aparecer repetidas
def busca_sequencial(lista, chave):
    indices = []
    for indice, elemento in enumerate(lista):
        if elemento == chave:
            indices.append(indice)
    return indices

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

def busca_binaria(lista, chave):
    lista = bubble_sort(lista)
    indices = []
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if lista[meio] < chave: #Se a chave for maior que o elemento encontrado
            inicio = meio + 1 #Joga a busca pra direita
        elif lista[meio] > chave: #Se a chave for menor que o elemento encontrado
            fim = meio - 1 #Joga a busca pra esquerda
        else: #Se a chave for IGUAL ao elemento encontrado (o que queremos)
            indices.append(meio) #Salva o índice na lista (pois o exercício pediu)

            esq = meio - 1
            while esq >= 0 and lista[esq] == chave:
                indices.append(esq)
                esq -= 1 #Anda uma casa pra esquerda

            dir = meio + 1
            while dir < len(lista) and lista[dir] == chave:
                indices.append(dir)
                dir += 1 #Anda uma casa pra direita

            #Como já varremos todos os lados a partir do ponto de encontro, podemos parar a busca principal (com o break)
            break

    indices.sort()
    return indices

chave = int(input("Digite a chave que busca procurar na lista de números inteiros: "))
lista = [10, 20, 20, 20, 30, 40, 40, 50, 60]

sequencial = busca_sequencial(lista, chave)
binaria = busca_binaria(lista, chave)

print(f"\nÍndices (busca sequencial): {sequencial}")
print(f"\nÍndices (busca binária): {binaria}")