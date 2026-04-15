#Verifica se um número é triangular
def verifica_triangular(valor, n):
    if n <= 0:
        return False
    else:
        if n * (n - 1) * (n - 2) == valor:
            lista = [n, n - 1, n - 2]
            return lista
        else:
            return verifica_triangular(valor, n - 1)

n = abs(int(input("Insira um número natural: ")))
valor = n
if n == 0 or n == 1 or n == 2:
    print("\nO número não é triangular.")
else:
    triangular = verifica_triangular(valor, n)
    if triangular == False:
        print("\nO número não é triangular.")
    else:
        natural1 = verifica_triangular(valor, n)[0]
        natural2 = verifica_triangular(valor, n)[1]
        natural3 = verifica_triangular(valor, n)[2]
        print(f"\nO número é triangular ({n} = {natural1} x {natural2} x {natural3}).")