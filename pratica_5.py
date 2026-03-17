#Função que recebe uma string como parâmetro e devolva outra string com os caracteres embaralhados
import random

def embaralha():
    palavra = str(input(f"Digite qualquer palavra: ")).lower().strip()
    lista = list(palavra)
    random.shuffle(lista)
    randomizada = "".join(lista)
    return randomizada

print(f"\nPalavra embaralhada: {embaralha()}")