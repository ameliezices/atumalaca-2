#Sequência de Tribonacci
def tribonacci(n):
    lista = [1, 1, 2]
    if n <= 3:
        lista = lista[:n]
    else:
        for _ in range(n - 3):
            lista.append(lista[-1] + lista[-2] + lista[-3])

    if n != 1:
        print(f"\nPrimeiros {n} elementos da sequência de Tribonacci: {lista}")
    else:
        print(f"{n}º elemento da sequência de Tribonacci: {lista}")

n = abs(int(input("Insira um número natural: ")))
if n == 0:
    print("\nValor inválido!")
else:
    tribonacci(n)