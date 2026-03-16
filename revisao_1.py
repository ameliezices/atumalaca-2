#Programa que, dados três números inteiros, imprime o maior deles

a = float(input("Digite o 1º valor: "))
b = float(input("Digite o 2º valor: "))
c = float(input("Digite o 3º valor: "))

maior = max(a, b, c)

print(f"\nO maior valor é {maior}")