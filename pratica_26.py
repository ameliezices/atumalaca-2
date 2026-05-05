#Função que lê o arquivo "notas.txt" e imprime os nomes dos estudantes que têm mais de seis notas registradas. Para cada estudante, também mostra a média aritmética de suas notas e determina os valores mínimo e máximo dentre elas
def analisa_arquivo(caminho_arquivo = "notas.txt"): #Define a função "analisa_arquivo", que possui como variável "caminho_arquivo" (perceba: essa é uma variável definida justamente nesta linha)
    with open(caminho_arquivo, "r", encoding = "utf-8") as f: #O comando "with (...) as (...)" anula a necessidade de fechar o arquivo depois. O parâmetro "encoding = 'utf-8'" é utilizado para que o programa, ao abrir o arquivo, identifique e grave corretamente caracteres especiais (emojis, acentos etc)
        for linha in f: #Lê uma linha de cada vez
            dados = linha.strip().split() #Separa os elementos da linha
            if len(dados) < 2: #Ignora linhas vazias ou sem conteúdo relevante
                continue #Faz com que pule para a próxima iteração (linha do arquivo "notas.txt")
            nome = dados[0]
            notas = [] #Lista que conterá as notas de cada aluno
            for i in dados[1:]: #Lê cada elemento da lista "dados", pulando o nome do aluno (dado pelo dados[0])
                try:
                    notas.append(float(i)) #Adiciona a nota à lista "notas"
                except ValueError: #Ignora palavras ou caracteres inválidos
                    continue #Faz com que pule para a próxima iteração (elemento da lista "dados")
            if len(notas) > 6: #Filtra os estudantes com mais de seis notas registradas
                media = sum(notas) / len(notas)
                menor = min(notas)
                maior = max(notas)
                print(f"Estudante: {nome}")
                print(f"Média: {media:.2f}")
                print(f"Valores máximo e mínimo: {maior:.2f} e {menor:.2f}")
                print("-" * 60) #Cria uma linha horizontal (decoração)

analisa_arquivo()