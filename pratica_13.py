#Função recursiva que recebe um número inteiro positivo n e calcula o somatório dos números de 1 a n
def soma(n):
    if n == 1:
        return 1
    else:
        return n + soma(n - 1)

x = int(input("Insira um número natural: "))
resultado = soma(x)
print(f"\nSoma dos elementos de 1 até n: {resultado}")