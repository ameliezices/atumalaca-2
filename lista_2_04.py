#Verificador de quadrado mágico
def imprimir_cabecalho():
    """Função para deixar a tela inicial mais bonita e organizada."""
    print("═" * 60)
    print("VERIFICADOR DE QUADRADO MÁGICO")
    print("═" * 60)
    print("Um quadrado mágico é uma matriz onde a soma das linhas,")
    print("colunas e diagonais é sempre a mesma.")
    print("═" * 60)

def criar_matriz(ordem):
    """Lê os valores da matriz digitados pelo usuário."""
    matriz = []
    print(f"\nDigite os {ordem * ordem} elementos da matriz:")
    for i in range(ordem):
        linha = []
        for j in range(ordem):
            while True:
                try:
                    valor = int(input(f"☐ Elemento [{i + 1}][{j + 1}]: "))
                    linha.append(valor)
                    break
                except ValueError:
                    print("⚠︎ Por favor, digite apenas números inteiros.")
        matriz.append(linha)
    return matriz

def mostrar_matriz(matriz, ordem):
    """Imprime a matriz de forma alinhada no console."""
    print("\nMatriz digitada:")
    for i in range(ordem):
        linha_formatada = ""
        for j in range(ordem):
            #{:>4} alinha o número à direita ocupando 4 espaços
            linha_formatada += f"{matriz[i][j]:>4} "
        print(linha_formatada)

def verificar_quadrado_magico(matriz, ordem):
    """Contém a lógica matemática para validar o quadrado mágico."""
    #Verificar se todos os elementos são distintos
    elementos = []
    for linha in matriz:
        elementos.extend(linha)
    if len(elementos) != len(set(elementos)):
        return False, "Existem elementos repetidos na matriz."
    #Definimos a "soma alvo" baseada na primeira linha
    soma_alvo = sum(matriz[0])
    #Verificar todas as linhas
    for i in range(ordem):
        if sum(matriz[i]) != soma_alvo:
            return False, f"A linha {i + 1} não soma {soma_alvo}."
    #Verificar todas as colunas
    for j in range(ordem):
        soma_coluna = 0
        for i in range(ordem):
            soma_coluna += matriz[i][j]
        if soma_coluna != soma_alvo:
            return False, f"A coluna {j + 1} não soma {soma_alvo}."
    #Verificar a diagonal principal
    soma_diag_princ = sum(matriz[i][i] for i in range(ordem))
    if soma_diag_princ != soma_alvo:
        return False, f"A diagonal principal não soma {soma_alvo}."
    #Verificar a diagonal secundária
    soma_diag_sec = sum(matriz[i][ordem - 1 - i] for i in range(ordem))
    if soma_diag_sec != soma_alvo:
        return False, f"A diagonal secundária não soma {soma_alvo}."
    return True, f"Todas as somas são iguais a {soma_alvo}."

def main():
    """Função principal que organiza a execução do programa."""
    imprimir_cabecalho()
    #Loop para garantir que o usuário digite um número válido para a ordem
    while True:
        try:
            ordem = int(input("\nDigite a ordem da matriz quadrada: "))
            if ordem < 2:
                print("⚠︎ A ordem deve ser no mínimo 2.")
            else:
                break
        except ValueError:
            print("⚠︎ Digite um número inteiro válido.")
    #Ler os dados
    matriz = criar_matriz(ordem)
    #Mostrar os dados de forma organizada
    mostrar_matriz(matriz, ordem)
    #Processar e verificar
    eh_magico, mensagem = verificar_quadrado_magico(matriz, ordem)
    #Exibir o resultado final
    print("\n" + "═" * 60)
    if eh_magico:
        print("É um quadrado mágico! (∩^o^∩)")
    else:
        print("Não é um quadrado mágico! (◔_◔)")
    print(f"Motivo: {mensagem}")
    print("═" * 60)

#Garante que o programa rode apenas quando executado diretamente
if __name__ == "__main__":
    main()