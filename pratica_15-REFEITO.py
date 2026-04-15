#Função recursiva que imprime todos os números pares de 0 até um determinado n
def acha_pares(n):
    if n < 0:
        return []

    pares = acha_pares(n - 1)
    if n % 2 == 0:
        pares.append(n)
    return pares

n = abs(int(input("Insira um número natural: ")))
pares = acha_pares(n)
print(f"\nValores pares de 0 até {n}: {pares}")