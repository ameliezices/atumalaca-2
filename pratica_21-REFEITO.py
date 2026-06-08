#Verifica se um número é triangular
def verifica_triangular(n, valor):
    if n <= 2:
        return False
    elif n * (n - 1) * (n - 2) == valor:
        return True
    else:
        return verifica_triangular(n - 1, valor)

n = abs(int(input("Insira um número natural não negativo: ")))
valor = n
resposta = verifica_triangular(n, valor)
if resposta:
    print("\nÉ um número triangular!")
else:
    print("\nNão é um número triangular!")