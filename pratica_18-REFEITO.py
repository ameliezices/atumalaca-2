#Dado um número natural n, calcular (2n)! + 3 * (soma de 1 até n) ** 3 + 4 * (soma de 1 até n) ** 4
def calcula_fatorial(n):
    if n == 1:
        return 1
    else:
        return n * calcula_fatorial(n - 1)

def calcula_somatoria(n, expoente):
    if n == 1:
        return 1
    else:
        somatoria = 0
        for i in range(1, n + 1):
            somatoria += i ** expoente
        return somatoria

n = abs(int(input("Insira um número natural não nulo: ")))
if n == 0:
    print("\nO valor não pode ser nulo.")
else:
    duplicado = 2 * n
    fatorial_duplicado = calcula_fatorial(duplicado)
    somatoria_ao_cubo = calcula_somatoria(n, 3)
    somatoria_a_quarta = calcula_somatoria(n, 4)
    resultado = fatorial_duplicado + 3 * somatoria_ao_cubo + 4 * somatoria_a_quarta
    print(f"\nResultado da equação: {resultado}")