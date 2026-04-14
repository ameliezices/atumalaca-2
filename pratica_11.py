#Função que recebe uma matriz e retorna sua transposta
def cria_matriz(linhas, colunas):
    m = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento [{i + 1}][{j + 1}]: ")))
        m.append(linha)
    return m

def mostra_matriz(m):
    l = len(m)
    for l in m:
        print(l)

def acha_transposta(m):
    colunas = len(m[0])
    linhas = len(m)
    transposta = []

    for i in range(colunas):
        linha = []
        for j in range(linhas):
            linha.append(m[j][i])
        transposta.append(linha)
    return transposta

print("Encontrando a transposta de uma matriz qualquer\n")
linhas = int(input("Insira a quantidade de linhas da matriz: "))
colunas = int(input("Insira a quantidade de colunas da matriz: "))
print()
matriz = cria_matriz(linhas, colunas)
print("\nMatriz fornecida:")
mostra_matriz(matriz)
transposta = acha_transposta(matriz)
print("\nMatriz transposta:")
mostra_matriz(transposta)