#Função recursiva que calcula a soma dos números inteiros de 1 a um determinado n
def soma_numeros(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n + soma_numeros(n - 1)

n = abs(int(input("Insira um número natural: ")))
soma = soma_numeros(n)
print(f"\nSoma dos inteiros de 1 até {n}: {soma}")