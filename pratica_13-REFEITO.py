#Função recursiva que calcula a soma dos números inteiros de 1 a um determinado n
def soma(n):
    if n == 1:
        return n
    else:
        n += soma(n - 1)
        return n

numero = abs(int(input("Digite um número natural: ")))
print(f"\nSoma dos inteiros de 1 até {numero}:")
print(soma(numero)) #PQPPPPPPPPPPPPPPPPPPPP EU SEI FAZER SOZINHA!!!!!!!!!!!