#Exercício extra da prática 3!
#Função que recebe duas matrizes e retorna a transposta da soma delas
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

def acha_transposta(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    transposta = []
    for i in range(colunas):
        linha = []
        for j in range(linhas):
            linha.append(matriz[j][i])
        transposta.append(linha)
    return transposta

def soma_matrizes(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    soma = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(matriz1[i][j] + matriz2[i][j])
        soma.append(linha)
    return soma

print("Encontrando a transposta da soma entre duas matrizes")

linhas_A = int(input("\nQuantidade de linhas da primeira matriz: "))
colunas_A = int(input("Quantidade de colunas da primeira matriz: "))
print(f"\nOrdem da primeira matriz: {linhas_A}x{colunas_A}")

linhas_B = int(input("\nQuantidade de linhas da segunda matriz: "))
colunas_B = int(input("Quantidade de colunas da segunda matriz: "))
print(f"\nOrdem da segunda matriz: {linhas_B}x{colunas_B}\n")

if linhas_A != linhas_B or colunas_A != colunas_B:
    print("Não é possível somar matrizes com diferentes ordens.")
else:
    print(f"Criando a primeira matriz (ordem {linhas_A}x{colunas_A}):\n")
    matriz_A = cria_matriz(linhas_A, colunas_A)
    print("\nPrimeira matriz:")
    mostra_matriz(matriz_A)

    print(f"\nCriando a segunda matriz (ordem {linhas_B}x{colunas_B}):\n")
    matriz_B = cria_matriz(linhas_B, colunas_B)
    print("\nSegunda matriz:")
    mostra_matriz(matriz_B)

    transposta_A = acha_transposta(matriz_A)
    transposta_B = acha_transposta(matriz_B)
    soma_transpostas = soma_matrizes(transposta_A, transposta_B)
    print("\nTransposta da soma entre as duas matrizes:")
    mostra_matriz(soma_transpostas)