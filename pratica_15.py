#Função recursiva que imprime todos os números pares de 0 até um determinado n
def acha_pares(numero):
    if numero < 0: #CASO BASE! Impede que a função continue infinitamente para os números negativos
        return []

    pares = acha_pares(numero - 1)

    if numero % 2 == 0:
        pares.append(numero)

    return pares

numero = abs(int(input("Insira um número natural: ")))
pares = acha_pares(numero)
print(f"\nNúmeros pares de 0 até {numero}: {pares}")