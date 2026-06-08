#Função que identifica matrizes identidade
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento {i + 1}x{j + 1}: ")))
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def cria_matriz_identidade(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            if i == j:
                linha.append(1)
            else:
                linha.append(0)
        matriz.append(linha)
    return matriz

def verifica_identidade(matriz, matriz_identidade):
    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] == matriz_identidade[i][j]:
                return True
            else:
                return False

linhas = abs(int(input("Determine a ordem da sua matriz: ")))
colunas = linhas
print("\nDeterminando a matriz:")
matriz = cria_matriz(linhas, colunas)
print("\nMatriz resultante:")
mostra_matriz(matriz)
print("\nVerificando se é uma matriz identidade...")
matriz_identidade = cria_matriz_identidade(linhas, colunas)
resposta = verifica_identidade(matriz, matriz_identidade)
if resposta:
    print("\nÉ uma matriz identidade!")
else:
    print("\nNão é uma matriz identidade!")