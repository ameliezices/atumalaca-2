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
    linha = len(matriz)
    for linha in matriz:
        print(linha)

def multiplica_matriz(matriz1, matriz2):
    linhas1 = len(matriz1)
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])
    nula = [[0 for _ in range(colunas2)]for _ in range(linhas1)]
    for i in range(linhas1):
        for j in range(colunas2):
            for k in range(linhas2):
                nula[i][j] += matriz1[i][k] * matriz2[k][j]
    return nula

print("Definindo o produto entre duas matrizes\n")
print("1. Matriz A")
linhasA = int(input("Quantidade de linhas da matriz A: "))
colunasA = int(input("Quantidade de colunas da matriz A: "))
print()
matrizA = cria_matriz(linhasA, colunasA)
print("\nMatriz A:")
mostra_matriz(matrizA)

print("\n2. Matriz B")
linhasB = int(input("Quantidade de linhas da matriz B: "))
colunasB = int(input("Quantidade de colunas da matriz B: "))
print()
if colunasA != linhasB:
    print("Não é possível multiplicar as matrizes A e B!")
else:
    matrizB = cria_matriz(linhasB, colunasB)
    print("\nMatriz B:")
    mostra_matriz(matrizB)
    produto = multiplica_matriz(matrizA, matrizB)
    print("\n3. Produto de A e B:")
    mostra_matriz(produto)