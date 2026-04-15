#Função recursiva que calcula a soma dos cubos de 1 até um determinado n
def soma_cubos(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n ** 3 + soma_cubos(n - 1)

n = abs(int(input("Insira um número natural: ")))
resultado = soma_cubos(n)
print(f"\nSoma dos cubos de 1 até {n}: {resultado}")