#Função que lê o arquivo "vendas.txt", calcula o total de vendas por vendedor, identifica o que teve o maior volume de vendas, determina o produto mais vendido e gera um arquivo nomeado "relatorio.txt" contendo essas informações
def gera_relatorio(caminho_arquivo = "vendas.txt"):
    vendas_por_vendedor = {}
    ocorrencias_por_produto = {}
    with open(caminho_arquivo, "r", encoding = "utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split()
            if len(dados) < 2:
                continue

            vendedor, produto, vendas = dados[0], dados[1], float(dados[2])

            if vendedor in vendas_por_vendedor:
                vendas_por_vendedor[vendedor] += vendas
            else:
                vendas_por_vendedor[vendedor] = vendas

            if produto in ocorrencias_por_produto:
                ocorrencias_por_produto[produto] += 1
            else:
                ocorrencias_por_produto[produto] = 1

    mais_vendedor = ""
    vendas_mais_vendido = 0
    for vendedor, vendas in vendas_por_vendedor.items():
        if vendas > vendas_mais_vendido:
            vendas_mais_vendido = vendas
            mais_vendedor = vendedor

    mais_vendido = ""
    ocorrencias_mais_vendido = 0
    for produto, ocorrencias in ocorrencias_por_produto.items():
        if ocorrencias > ocorrencias_mais_vendido:
            ocorrencias_mais_vendido = ocorrencias
            mais_vendido = produto

    with open("relatorio.txt", "w", encoding = "utf-8") as relatorio:
        relatorio.write(f"Vendedor com maior volume de vendas: {mais_vendedor} ({vendas_mais_vendido:.0f} vendas)\n")
        relatorio.write(f"Produto com mais ocorrências: {mais_vendido} ({ocorrencias_mais_vendido} ocorrências)")

gera_relatorio()