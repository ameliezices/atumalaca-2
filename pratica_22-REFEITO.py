#Função que imprime os n primeiros números da sequência de Tribonacci
def tribonacci(n):
    termos = [1, 1, 2]
    if n <= 3:
        sequencia = []
        for i in range(n):
            sequencia.append(termos[i])
        return sequencia
    else:
        for i in range(n - 3):
            termos.append(termos[i] + termos[i + 1] + termos[i + 2])
        return termos

n = abs(int(input("Insira um número natural não nulo: ")))
if n == 0:
    print("\nO valor não pode ser nulo!")
else:
    if n == 1:
        print(f"\nO primeiro termo da sequência de Fibonacci é:")
    else:
        print(f"\nOs {n} primeiros termos da sequência de Tribonacci são:")
    sequencia = tribonacci(n)
    print(sequencia)