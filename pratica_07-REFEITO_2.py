#Função que recebe duas matrizes e retorna o produto delas
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

def multiplica_matrizes(matriz1, matriz2):
    linhas1 = len(matriz1)
    linhas2 = len(matriz2)
    colunas2 = len(matriz2[0])

    nula = [[0 for _ in range(colunas2)] for _ in range(linhas1)]

    for i in range(linhas1):
        for j in range(colunas2):
            for k in range(linhas2):
                nula[i][j] += matriz1[i][k] * matriz2[k][j]
    return nula

print("Definindo o produto entre duas matrizes")

linhas_A = int(input("\nQuantidade de linhas da primeira matriz: "))
colunas_A = int(input("Quantidade de colunas da primeira matriz: "))
print(f"\nOrdem da primeira matriz: {linhas_A}x{colunas_A}")

linhas_B = int(input("\nQuantidade de linhas da segunda matriz: "))
colunas_B = int(input("Quantidade de colunas da segunda matriz: "))
print(f"\nOrdem da segunda matriz: {linhas_B}x{colunas_B}\n")

if colunas_A != linhas_B:
    print("Não é possível multiplicar matrizes com essas ordens.")
else:
    print(f"Criando a primeira matriz (ordem {linhas_A}x{colunas_A})\n")
    matriz_A = cria_matriz(linhas_A, colunas_A)
    print("\nPrimeira matriz:")
    mostra_matriz(matriz_A)

    print(f"\nCriando a segunda matriz (ordem {linhas_B}x{colunas_B})\n")
    matriz_B = cria_matriz(linhas_B, colunas_B)
    print("\nSegunda matriz:")
    mostra_matriz(matriz_B)

    produto = multiplica_matrizes(matriz_A, matriz_B)
    print("\nProduto entre as duas matrizes:")
    mostra_matriz(produto)