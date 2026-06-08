#Soma de 1 até um determinado valor n, mas os números ímpares são negativos enquanto os pares são positivos
def calcula_soma(n):
    if n == 1:
        return -1
    elif n % 2 == 0:
        return n + calcula_soma(n - 1)
    else:
        return -n + calcula_soma(n - 1)

n = abs(int(input("Insira um número natural não nulo: ")))
if n == 0:
    print("\nO valor não pode ser nulo.")
else:
    resultado = calcula_soma(n)
    print(f"\nResultado: {resultado}")