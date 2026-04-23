#Função que recebe uma lista com dois ou mais números inteiros positivos e retorna o MDC e o MMC entre eles
def calcula_mdc(a, b):
    if b == 0:
        return a
    else:
        return calcula_mdc(b, a % b)

def calcula_mmc(a, b):
    if a == b:
        return a
    else:
        return (a * b) // calcula_mdc(a, b)

def devolve_mdc(lista):
    #Não sei como passar os elementos da lista pelo MMC e MDC

def devolve_mmc(lista):
    #Não sei como passar os elementos da lista pelo MMC e MDC

lista = []
print()
if quantidade < 2:
    print("Quantia inválida!")
else:
    for i in range(quantidade):
        lista.append(abs(int(input(f"Insira o {i + 1}º elemento: "))))

    mdc = devolve_mdc(lista)
    mmc = devolve_mmc(lista)

    print(f"\nMMC de {lista}: {mmc}")
    print(f"MDC de {lista}: {mdc}")