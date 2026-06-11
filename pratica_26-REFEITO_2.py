#Função que lê o arquivo "notas.txt", imprime o nome dos estudantes com mais de seis notas registradas, calcula a média aritmética de suas respectivas notas e devolve os valores máximo e mínimo dentre elas
def analisa_notas(caminho_arquivo = "notas.txt"):
    alunos = {}
    alunos_mais_de_seis_notas = []
    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split()
            if len(dados) < 2:
                continue

            aluno = dados[0]

            notas = []
            for nota in dados[1:]:
                try:
                    notas.append(float(nota))
                except ValueError:
                    continue

            if len(notas) > 6:
                alunos_mais_de_seis_notas.append(aluno)

            informacoes = {
                "media": sum(notas) / len(notas),
                "maior": max(notas),
                "menor": min(notas)
            }

            alunos[aluno] = informacoes

    with open("analise.txt", "w", encoding = "utf-8") as analise:
        analise.write(f"Alunos com mais de seis notas registradas: {alunos_mais_de_seis_notas}\n\n")
        analise.write(f"=" * 80)
        analise.write(f"\n\nInformações gerais:")
        for aluno, informacoes in alunos.items():
            analise.write(f"\n\nAluno: {aluno}\n")
            analise.write(f"- Média: {informacoes["media"]:.2f}\n")
            analise.write(f"- Maior e menor nota: {informacoes["maior"]:.2f} e {informacoes["menor"]:.2f}, respectivamente")

analisa_notas()