#Soma de 1 até um determinado valor n, mas os números ímpares são negativos enquanto os pares são positivos
def soma_numeros(n):
    if n == 1:
        return -1
    elif n % 2 == 0:
        return n + soma_numeros(n - 1)
    else:
        return -n + soma_numeros(n - 1)

n = abs(int(input("Insira um número natural: ")))
if n == 0:
    print("\nO número inserido não pode ser 0.")
else:
    soma = soma_numeros(n)
    print(f"\nSoma dos pares e subtração dos ímpares de 1 até {n}: {soma}")