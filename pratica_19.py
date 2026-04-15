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

def acha_menor(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    menor = matriz[0][0]
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] < menor:
                menor = matriz[i][j]
    return menor

print("Identificando o menor elemento de uma matriz")
linhas = abs(int(input("\nDetermine o número de linhas: ")))
colunas = abs(int(input("Determine o número de colunas: ")))

print()
matriz = cria_matriz(linhas, colunas)
print("\nMatriz fornecida:")
mostra_matriz(matriz)

print(f"\nMenor elemento: {acha_menor(matriz)}")