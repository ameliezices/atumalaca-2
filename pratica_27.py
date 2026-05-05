#Mesma coisa do exercício anterior, mas a diferença é que agora o arquivo a ser lido é o "notas.csv"
def analisa_notas(caminho_arquivo = "notas.csv"):
    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip() #Remove espaços desnecessários
            if not linha: #Pula linhas vazias
                continue

            dados = linha.split(",") #É aqui que o programa difere do programa feito na prática 26! Ele separa os elementos de cada linha usando o caractere "," como parâmetro
            nome = dados[0]
            notas = []

            for nota in dados[1:]:
                try:
                    notas.append(float(nota))
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