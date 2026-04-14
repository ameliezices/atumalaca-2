#Função recursiva que calcula a soma dos cubos de 1 até um determinado n
def soma_cubo(numero):
    if numero == 1:
        return numero
    else:
        return numero ** 3 + soma_cubo(numero - 1)

numero = abs(int(input("Insira um número natural: ")))
print(f"\nSoma dos cubos de 1 até {numero}:")
print(soma_cubo(numero))