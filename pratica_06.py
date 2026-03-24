#Função que recebe duas matrizes A e B e retorna a somatória delas
def recebe_matriz_A():
    for i in range(linhas_A):
        linha = []
        for j in range(colunas_A):
            elementos = float(input(f"Elemento {[i + 1]}{[j + 1]} da matriz A: "))
            linha.append(elementos)
        matriz_A.append(linha)

def recebe_matriz_B():
    for i in range(linhas_B):
        linha = []
        for j in range(colunas_B):
            elementos = float(input(f"Elemento {[i + 1]}{[j + 1]} da matriz B: "))
            linha.append(elementos)
        matriz_B.append(linha)

def somatoria():
    for i in range(linhas_A):
        linha = []
        for j in range(colunas_A):
            elementos = matriz_A[i][j] + matriz_B[i][j]
            linha.append(elementos)
        matriz_C.append(linha)
    print(matriz_C)

print("Soma de duas matrizes\n")
linhas_A = int(input(f"Insira a quantidade de linhas da matriz A: "))
colunas_A = int(input(f"Insira o número de colunas da matriz A: "))
print()
matriz_A = []
recebe_matriz_A()

print()

linhas_B = int(input(f"Insira a quantidade de linhas da matriz B: "))
colunas_B = int(input(f"Insira o número de colunas da matriz B: "))

print()

for h in range(1):
    if (linhas_A != linhas_B) or (colunas_A != colunas_B):
        print("Não é possível somar as duas matrizes.")
    else:
        matriz_B = []
        recebe_matriz_B()

        print(f"\nMatriz C:")
        matriz_C = []
        somatoria()