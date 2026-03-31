#Função que retorna a letra mais comum em uma dada string
string = input("Entre com uma string: ")
registro = {}

for letra in string:
    if letra in registro:
        registro[letra] += 1
    else:
        registro[letra] = 1

frequente = ""

for chave in registro:
    if not frequente:
        frequente = chave
    elif registro[chave] > registro[frequente]:
        frequente = chave

print(f"\nLetra mais frequente: {frequente}")