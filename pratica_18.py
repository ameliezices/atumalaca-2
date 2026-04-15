#Dado um número natural n, calcular (2n)! + 3 * (soma de 1 até n) ** 3 + 4 * (soma de 1 até n) ** 4
def calcula_fatorial(duplicado):
    if duplicado == 1:
        return 1
    else:
        return duplicado * calcula_fatorial(duplicado - 1)

def somatorio_expoente(n, m):
    if n == 1:
        return 1
    else:
        return (n ** m) + somatorio_expoente(n - 1, m)

n = abs(int(input("Insira um número natural: ")))

if n == 0:
    print("\nO valor inserido não pode ser 0.")
else:
    duplicado = n * 2
    fatorial = calcula_fatorial(duplicado)
    soma_cubos = somatorio_expoente(n, 3)
    soma_quartas = somatorio_expoente(n, 4)

    resultado = fatorial + 3 * (soma_cubos) + 4 * (soma_quartas)

    print(f"\nFatorial duplo: {duplicado}! = {fatorial}")
    print(f"Somatória dos cubos: {soma_cubos}")
    print(f"Somatória das quartas: {soma_quartas}")
    print(f"\nResultado da equação: {resultado}")