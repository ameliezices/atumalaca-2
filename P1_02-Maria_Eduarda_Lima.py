#Função que recebe duas matrizes e devolve o produto delas
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

def multiplica_matriz(matriz_A, matriz_B):
    linhas_A = len(matriz_A)
    linhas_B = len(matriz_B)
    colunas_B = len(matriz_B[0])
    nula = [[0 for _ in range(colunas_B)] for _ in range(linhas_A)]

    for i in range(linhas_A):
        for j in range(colunas_B):
            for k in range(linhas_B):
                nula[i][j] += matriz_A[i][k] * matriz_B[k][j]
    return nula

linhas_A = abs(int(input("Insira a quantidade de linhas da matriz A: ")))
colunas_A = abs(int(input("Insira a quantidade de colunas da matriz A: ")))

linhas_B = abs(int(input("\nInsira a quantidade de linhas da matriz B: ")))
colunas_B = abs(int(input("Insira a quantidade de colunas da matriz B: ")))

if colunas_A != linhas_B:
    print("\nNão é possível multiplicar as matrizes fornecidas.")
else:
    print("\nDefinindo a matriz A\n")
    matriz_A = cria_matriz(linhas_A, colunas_A)
    print("\nMatriz A:")
    mostra_matriz(matriz_A)

    print("\nDefinindo a matriz B\n")
    matriz_B = cria_matriz(linhas_B, colunas_B)
    print("\nMatriz B:")
    mostra_matriz(matriz_B)

    produto = multiplica_matriz(matriz_A, matriz_B)
    print("\nProduto entre A e B:")
    mostra_matriz(produto)