#Calcular a soma n/1 + (n - 1)/2 + (n - 2)/3 + ... + 1/n
def calcula_soma(n):
    soma = 0
    for i in range(1, n + 1):
        soma += (n - i + 1) / i
    return soma

n = abs(int(input("Insira um número natural: ")))
fixo = n
soma = calcula_soma(n)
print(f"\nResultado da equação: {soma}")