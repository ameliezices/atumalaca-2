#Recebe duas strings distintas e os nomes de dois arquivos distintos. O primeiro arquivo deve haver uma frase hipoteticamente contendo a primeira string fornecida. Devemos gerar o segundo arquivo de maneira que ele tenha em sua estrutura a mesma frase do primeiro arquivo, mas substituindo as aparições da primeira string pela segunda string
def troca_strings_arquivos(caminho_arquivo_1, caminho_arquivo_2, string_1, string_2):
    try:
        with open(caminho_arquivo_1, "r", encoding = "utf-8") as arquivo_1:
            conteudo_original = arquivo_1.read()

        conteudo_substituido = conteudo_original.replace(string_1, string_2)

        with open(caminho_arquivo_2, "w", encoding = "utf-8") as arquivo_2:
            arquivo_2.write(conteudo_substituido)

        return "Troca de strings realizada com sucesso!"
    except FileNotFoundError:
        return f"Erro: O arquivo '{caminho_arquivo_1}' não foi encontrado."
    except Exception as e:
        return f"Ocorreu um erro inesperado: '{e}'"

def main():
    arquivo_1 = input("Digite o nome do primeiro arquivo: ")
    arquivo_2 = input("Digite o nome do segundo arquivo: ")

    string_1 = input("Insira a string a ser substituída: ")
    string_2 = input("Insira a string que substituirá: ")

    resultado = troca_strings_arquivos(arquivo_1, arquivo_2, string_1, string_2)
    print(f"\n{resultado}")

def cria_arquivo(nome_arquivo, conteudo):
    with open(nome_arquivo, "w", encoding = "utf-8") as arquivo:
        arquivo.write(conteudo)
    return f"Arquivo '{nome_arquivo}' criado com sucesso!\n"

if __name__ == "__main__":
    #Descomente a linha abaixo (remova o #) para criar um arquivo "arquivo_1.txt" automaticamente
    #cria_arquivo("arquivo_1.txt", "Eu amo gatos! Gatos são animais incríveis e eu amo gatos.")
    main()