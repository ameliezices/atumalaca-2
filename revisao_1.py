#Programa que, dados três números inteiros, imprime o maior deles.
a = print(input("Digite um número: "))
b = print(input("Digite um número: "))
c = print(input("Digite um número: "))

if a >= b and a >= c:
    print(f"O maior número fornecido é {a}")
elif b >= c:
    print(f"O maior número fornecido é {b}")