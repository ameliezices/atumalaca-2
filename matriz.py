#Modelo para a criação de matrizes
def cria_matriz(linhas, colunas):
    m = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento [{i + 1}][{j + 1}]: ")))
        m.append(linha)
    return m

def printa_matriz(m):
    for i in range(linhas):
        print(m[i])

def matriz_nula(coluna, linha):
    nula = [[0 for _ in range(coluna)] for _ in range(linha)]
    return nula

def soma(matriz1, matriz2):
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz1[i][j] + matriz2[i][j])
        matriz.append(linha)
    return matriz

linhas = int(input("Insira o número de linhas da matriz: "))
colunas = int(input("Insira o número de colunas da matriz: "))
matriz1 = cria_matriz(linhas, colunas)
printa_matriz(matriz1)
matriz2 = cria_matriz(linhas, colunas)
printa_matriz(matriz2)
matriz = []
print(soma(matriz1, matriz2))