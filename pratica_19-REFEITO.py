#Função que encontra o menor elemento de uma matriz fornecida
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento [{i + 1}][{j + 1}]: ")))
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def verifica_elementos(matriz):
    menor_elemento = matriz[0][0]
    for linha in matriz:
        for elemento in linha:
            if elemento < menor_elemento:
                menor_elemento = elemento
    return menor_elemento

linhas = abs(int(input("Insira a quantidade de linhas desejada para a sua matriz: ")))
colunas = abs(int(input("Insira a quantidade de colunas desejada para a sua matriz: ")))
print("\nConstruindo a matriz:")
matriz = cria_matriz(linhas, colunas)
print("\nMatriz fornecida:")
mostra_matriz(matriz)
menor = verifica_elementos(matriz)
print(f"\nMenor elemento da matriz: {menor}")