#Função que recebe uma lista com dois ou mais números e retorna o MMC e o MDC entre eles
def mdc(a, b):
    a, b = abs(a), abs(b)
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
    if a == 0 or b == 0:
        return 0
    else:
        return abs(a * b) // mdc(a, b)

print("Definindo o MMC e o MDC de números inteiros pertencentes a uma lista\n")
quantidade = int(input("Insira a quantidade de elementos da sua lista: "))
print()

if quantidade < 2:
    print(f"Erro: a lista deve conter ao menos dois elementos!")
else:
    lista = [int(input(f"Insira o {_ + 1}º elemento: ")) for _ in range(quantidade)]

    mdc_lista = lista[0]
    for i in range(1, len(lista)):
        mdc_lista = mdc(mdc_lista, lista[i])

    mmc_lista = lista[0]
    for i in range(1, len(lista)):
        mmc_lista = mmc(mmc_lista, lista[i])

    print(f"\nLista inserida: {lista}")
    print(f"\nMDC entre os elementos da lista: {mdc_lista}")
    print(f"MMC entre os elementos da lista: {mmc_lista}")