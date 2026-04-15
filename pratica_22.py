#Função que imprime os n primeiros números da sequência de Tribonacci
def tribonacci(n):
    lista = [1, 1, 2]

    if n <= 3:
        lista = lista[:n]
    else:
        for _ in range(n - 3):
            elemento = lista[-1] + lista[-2] + lista[-3]
            lista.append(elemento)

    if n >= 2:
        print(f"\nOs primeiros {n} termos da sequência de Tribonacci são:")
        print(lista)
    elif n == 1:
        print("\nO primeiro termo da sequência de Tribonacci é:")
        print(lista)

n = abs(int(input("Insira um número inteiro positivo: ")))
if n == 0:
    print("\nValor inválido!")
else:
    tribonacci(n)