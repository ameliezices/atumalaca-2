#Função que lê o arquivo "vendas.txt", calcula o total de vendas por vendedor, identifica o que teve o maior volume de vendas, determina o produto mais vendido e gera um arquivo nomeado "relatorio.txt" contendo essas informações
def gera_relatorio(caminho_arquivo = "vendas.txt"):
    vendas_por_vendedor = {}
    ocorrencia_do_produto = {}
    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip().split()
            if not linha:
                continue

            vendedor, produto, quantidade = linha[0], linha[1], float(linha[2])
            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += quantidade
            else:
                vendas_por_vendedor[vendedor] = quantidade

            if produto in ocorrencia_do_produto:
                ocorrencia_do_produto[produto] += 1
            else:
                ocorrencia_do_produto[produto] = 1

    melhor_vendedor = ""
    mais_vendas = 0

    for vendedor, quantidade in vendas_por_vendedor.items():
        if quantidade > mais_vendas:
            mais_vendas = quantidade
            melhor_vendedor = vendedor

    produto_mais_vendido = ""
    ocorrencias = 0

    for produto, ocorrencia in ocorrencia_do_produto.items():
        if ocorrencia > mais_vendas:
            mais_vendas = ocorrencia
            produto_mais_vendido = produto

    print(f"Melhor vendedor: {melhor_vendedor} ({quantidade} vendas)")
    print(f"Produto mais vendido: {produto_mais_vendido}")

gera_relatorio()