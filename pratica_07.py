#Função que recebe duas matrizes e retorna o produto delas
def cria_matriz(linhas, colunas):
    m = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento {[i + 1]}[{j + 1}]: ")))
        m.append(linha)
    return m

def mostra_matriz(m):
    for linha in m:
        print(linha)

def multiplica_matriz(matriz1, matriz2):
    linhas1 = len(matriz1)
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])

    matriz = [[0 for _ in range(colunas2)] for _ in range(linhas1)]

    for i in range(linhas1):
        for j in range(colunas2):
            for k in range(linhas2):
                matriz[i][j] += matriz1[i][k] * matriz2[k][j]

    return matriz

linhas1 = int(input("Insira a quantidade de linhas da primeira matriz: "))
colunas1 = int(input("Insira a quantidade de colunas da primeira matriz: "))
print()
matriz1 = cria_matriz(linhas1, colunas1)
print("\nPrimeira matriz:")
mostra_matriz(matriz1)

linhas2 = int(input("\nInsira a quantidade de linhas da segunda matriz: "))
colunas2 = int(input("Insira a quantidade de colunas da segunda matriz: "))
print()
if linhas2 != colunas1:
    print("Não é possível multiplicar as matrizes fornecidas.")
else:
    matriz2 = cria_matriz(linhas2, colunas2)
    print("\nSegunda matriz:")
    mostra_matriz(matriz2)

    resultado = multiplica_matriz(matriz1, matriz2)
    print("\nMultiplicação das matrizes:")
    mostra_matriz(resultado)