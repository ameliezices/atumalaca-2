#Função que identifica matrizes identidade
def cria_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento [{i + 1}][{j + 1}]: ")))
        matriz.append(linha)
    return matriz

def cria_identidade(linhas, colunas):
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

def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)

def identifica_igualdade(matriz1, matriz2):
    linhas = len(matriz1)
    colunas = len(matriz1[0])
    for i in range(linhas):
        for j in range(colunas):
            if matriz1[i][j] == matriz2[i][j]:
                return True
            else:
                return False

print("Verificando se uma dada matriz é uma matriz identidade")
linhas = abs(int(input("\nInsira a quantidade de linhas da sua matriz: ")))
colunas = abs(int(input("Insira a quantidade de colunas da sua matriz: ")))

if linhas != colunas:
    print("\nNão é uma matriz identidade.")
else:
    print()
    matriz = cria_matriz(linhas, colunas)
    print("\nMatriz fornecida:")
    mostra_matriz(matriz)

    identidade = cria_identidade(linhas, colunas)
    if identifica_igualdade(matriz, identidade):
        print("\nÉ uma matriz identidade.")
    else:
        print("\nNão é uma matriz identidade.")