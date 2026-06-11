#Mesma coisa do exercício anterior, mas a diferença é que agora o arquivo a ser lido é o "notas.csv"
def analisa_notas(caminho_arquivo = "notas.csv"):
    alunos_mais_de_seis_notas = []
    alunos = {}

    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.split(",")
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

    print(f"Alunos com mais de seis notas cadastradas: {alunos_mais_de_seis_notas}\n")
    print("=" * 55)
    print(f"\nInformações gerais:")
    for aluno, informacoes in alunos.items():
        print(f"\nAluno: {aluno}")
        print(f"- Média: {informacoes["media"]:.2f}")
        print(f"- Maior e menor nota: {informacoes["maior"]:.2f} e {informacoes["menor"]:.2f}, respectivamente")

analisa_notas()