#Função que lê o arquivo "notas.txt", imprime o nome dos estudantes com mais de seis notas registradas, calcula a média aritmética de suas respectivas notas e devolve os valores máximo e mínimo dentre elas
def analisa_notas(caminho_arquivo = "notas.txt"):
    alunos = {}
    mais_de_seis_notas = []
    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split()
            if len(dados) < 2: #Filtra linhas com conteúdo inútil
                continue #Pula pra próxima iteração (linha do arquivo)

            nome = dados[0]
            notas = []
            for nota in dados[1:]:
                try:
                    notas.append(float(nota))
                except ValueError:
                    continue #Pula pra próxima iteração (nota da lista dados)

            if len(notas) > 6:
                mais_de_seis_notas.append(nome)

            media = sum(notas) / len(notas)
            menor = min(notas)
            maior = max(notas)

            informacoes = {
                "media": media,
                "maior nota": maior,
                "menor nota": menor
            }

            alunos[nome] = informacoes

    print(f"Alunos com mais de seis notas: {mais_de_seis_notas}\n")
    print("=" * 75)
    print(f"\nAnálise geral:")
    for nome, informacoes in alunos.items():
        print(f"\nAluno: {nome}")
        print(f"- Média: {informacoes["media"]:.2f}")
        print(f"- Maior nota: {informacoes["maior nota"]:.2f}")
        print(f"- Menor nota: {informacoes["menor nota"]:.2f}")

analisa_notas()