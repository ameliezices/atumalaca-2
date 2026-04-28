try:
    arquivo = open("notas.txt", "r")
    linhas = arquivo.readline()
    lista_nomes = []
    while linhas:
        dados = linhas.split()
        if len(dados) > 7:
            lista_nomes.append(dados[0])
        linhas = arquivo.readline()
    lista_nomes = ", ".join(lista_nomes)
    arquivo.close()
    print(f"Estudantes: {lista_nomes}")
except:
    print("Não foi possível abrir o arquivo.")