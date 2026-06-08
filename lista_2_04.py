#Verificador de quadrado mágico
def imprimir_cabecalho():
    #Função apenas para deixar a tela inicial mais bonita e organizada
    print("═" * 75)
    print("VERIFICADOR DE QUADRADO MÁGICO")
    print("═" * 75)
    print("Um quadrado mágico é uma matriz onde a soma das linhas, colunas e diagonais")
    print("é sempre a mesma.")
    print("═" * 75)

def cria_matriz(ordem):
    #Lê os valores da matriz digitados pelo usuário
    matriz = []
    print(f"\n☐ Digite os {ordem * ordem} elementos da matriz:")

    for i in range(ordem):
        linha = []
        for j in range(ordem):
            while True:
                try:
                    valor = int(input(f"╰┈➤ Elemento [{i + 1}]x[{j + 1}]: "))
                    linha.append(valor)
                    break #Sai do loop se o número for válido
                except ValueError:
                    print("⚠︎ Por favor, digite apenas números inteiros.")
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz, ordem):
    #Imprime a matriz de forma alinhada no console
    print("\n☐ Matriz digitada:")
    for i in range(ordem):
        linha_formatada = ""
        for j in range(ordem):
            #{:>3} significa: alinhe o número à direita ocupando 3 espaços
            linha_formatada += f"{matriz[i][j]:>4} "
        print(linha_formatada)

def verificar_quadrado_magico(matriz, ordem):
    #Contém a lógica matemática para validar o quadrado mágico

    #Definimos a "soma alvo" baseada na primeira linha
    soma_alvo = sum(matriz[0])

    #Verificar todas as linhas
    for i in range(ordem):
        if sum(matriz[i]) != soma_alvo:
            return False, "As linhas não possuem a mesma soma."

    #Verificar todas as colunas
    for j in range(ordem):
        soma_coluna = 0
        for i in range(ordem):
            soma_coluna += matriz[i][j]  # Soma os elementos da coluna j
        if soma_coluna != soma_alvo:
            return False, "As colunas não possuem a mesma soma."

    #Verificar a diagonal principal
    soma_diag_princ = 0
    for i in range(ordem):
        soma_diag_princ += matriz[i][i]
    if soma_diag_princ != soma_alvo:
        return False, "A diagonal principal não bate com a soma alvo."

    #Verificar a diagonal secundária
    #A coluna diminui conforme a linha aumenta: ordem - 1 - i
    soma_diag_sec = 0
    for i in range(ordem):
        soma_diag_sec += matriz[i][ordem - 1 - i]
    if soma_diag_sec != soma_alvo:
        return False, "A diagonal secundária não bate com a soma alvo."

    return True, f"Todas as somas são iguais a {soma_alvo}."

imprimir_cabecalho()
#Loop para garantir que o usuário digite um número válido para a ordem
while True:
    try:
        ordem = int(input("\n☐ Digite a ordem da matriz quadrada: "))
        if ordem < 2:
            print("⚠︎ A ordem deve ser no mínimo 2.")
        else:
                break
    except ValueError:
        print("⚠︎ Digite um número inteiro válido.")

#Passo 1: Ler os dados
matriz = cria_matriz(ordem)

#Passo 2: Mostrar os dados de forma organizada
mostra_matriz(matriz, ordem)

#Passo 3: Processar e verificar
eh_magico, mensagem = verificar_quadrado_magico(matriz, ordem)

#Passo 4: Exibir o resultado final
print("\n" + "═" * 75)
if eh_magico:
    print("É um quadrado mágico! (∩^o^∩)")
else:
    print("Não é um quadrado mágico! (◔_◔)")
print(f"Motivo: {mensagem}")
print("═" * 75)