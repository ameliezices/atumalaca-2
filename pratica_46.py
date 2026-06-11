#Função recursiva que calcula os n primeiros valores da série harmônica
def calcula_serie_harmonica(n):
    if n == 1:
        return 1
    else:
        return (1 / n) + calcula_serie_harmonica(n - 1)

n = abs(int(input("Insira um número natural não nulo: ")))
if n == 0:
    print("\nErro: O valor inserido não pode ser nulo.")
else:
    print(f"\n{calcula_serie_harmonica(n)}")