#Função que recebe 3 números inteiros e verifica se a soma de qualquer par deles gera o terceiro número
def verifica_pares(a, b, c):
    if a + b == c:
        return True
    elif b + c == a:
        return True
    elif a + c == b:
        return True
    else:
        return False

lista = [int(input(f"Insira o {_ + 1}º número inteiro: ")) for _ in range(3)]
resultado = verifica_pares(lista[0], lista[1], lista[2])
if resultado:
    print("\nSim, a soma de quaisquer dois dos números fornecidos resulta no terceiro.")
else:
    print("\nNão, a soma de quaisquer dois dos números fornecidos não resulta no terceiro.")