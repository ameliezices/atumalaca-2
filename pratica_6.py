#Função que recebe duas matrizes A e B e retorna a somatória delas
def coleta_matriz_1():
    linhas1 = int(input("Insira o número de linhas da primeira matriz: "))
    colunas1 = int(input("Insira o número de colunas da primeira matriz: \n"))
    matriz1 = []
    linha1 = []

    for i in range(linhas1):
        for j in range(colunas1):
            elemento1 = float(input(f"Elemento [{i + 1}][{j + 1}]: ")).strip()
            linha1.append(elemento1)
        matriz1.append(linha1)

def coletar_matriz_2():
    linhas2 = int(input("\nInsira o número de linhas da segunda matriz: "))
    colunas2 = int(input("Insira o número de colunas da segunda matriz: \n"))
    matriz2 = []
    linha2 = []

    for i in range(linhas2):
        for j in range(colunas2):
            elemento2 = float(input(f"Elemento [{i + 1}][{j + 1}]: ")).strip()
            linha2.append(elemento2)
        matriz2.append(linha2)

def verifica_soma():
    linhas1 = len(coleta_matriz_1())
    colunas1 = len(coleta_matriz_1([0]))
    linhas2 = len(coletar_matriz_2())
    colunas2 = len(coletar_matriz_2([0]))
    if