#Função recursiva que calcula o fatorial duplo de um valor inteiro não negativo
def calcula_fatorial_duplo(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcula_fatorial_duplo(n - 2)

n = abs(int(input("Insira um número natural: ")))
fatorial_duplo = calcula_fatorial_duplo(n)
print(f"\nFatorial duplo de {n}: {fatorial_duplo}")