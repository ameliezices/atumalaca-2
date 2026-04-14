#Função que diz se uma matriz é simétrica (igual à sua transposta)
def cria_matriz(linhas, colunas):
    m = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(float(input(f"Elemento [{i + 1}][{j + 1}]: ")))
        m.append(linha)
    return m

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

def eh_simetrica(matriz, transposta):
    if linhas == colunas:
        for i in range(linhas):
            for j in range(colunas):
                if matriz[i][j] == matriz[j][i]:
                    return True
                else:
                    return False
    else:
        return False

print("Definindo se uma matriz é simétrica\n")
linhas = int(input("Quantidade de linhas da matriz: "))
colunas = int(input("Quantidade de colunas da matriz: "))
print()
matriz = cria_matriz(linhas, colunas)
print("\nMatriz fornecida:")
mostra_matriz(matriz)
transposta = acha_transposta(matriz)
print("\nMatriz transposta:")
mostra_matriz(transposta)
print("\nPortanto, é simétrica?")
if eh_simetrica(matriz, transposta):
    print("Sim!")
else:
    print("Não!")