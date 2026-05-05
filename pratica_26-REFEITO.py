#Função que lê o arquivo "notas.txt", imprime o nome dos estudantes com mais de seis notas registradas, calcula a média aritmética de suas respectivas notas e devolve os valores máximo e mínimo dentre elas
def analisa_notas(caminho_arquivo = "notas.txt"):
    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split()
            if len(dados) < 2:
                continue

            nome = dados[0]
            notas = []

            for i in dados[1:]:
                try:
                    notas.append(float(i))
                except ValueError:
                    continue

            if len(notas) > 6:
                media = sum(notas) / len(notas)
                maximo = max(notas)
                minimo = min(notas)

                print(f"Estudante: {nome}")
                print(f"Notas: {notas}")
                print(f"Média: {media:.2f}")
                print(f"Notas máxima e mínima: {maximo:.2f} e {minimo:.2f}")
                print("-" * 60)

analisa_notas()