#Calcular a soma apresentada no enunciado
def calcula_soma(n, fixo):
    if n == 1:
        return 1 / fixo
    else:
        lista = [i for i in range(1, n + 1)]
        fixo += calcula_soma(fixo - (n - 1), fixo) / lista[n - 1]
        return fixo

n = abs(int(input("Insira um número natural: ")))
fixo = n
soma = calcula_soma(n, fixo)
print(f"\nResultado da equação: {soma}")