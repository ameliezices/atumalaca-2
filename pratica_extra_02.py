#Exercício extra da prática 4!
#Função recursiva que retorna a soma dos dígitos de um determinado número
def soma_digitos(n):
    digitos = [digito for digito in n if digito.isdigit()]
    if len(digitos) == 1:
        return digitos[0]
    else:
        return int(digitos[0]) + int(soma_digitos(digitos[1:]))

print("Somando os dígitos de um número natural")
n = str(input("\nInsira um número natural: "))
soma = soma_digitos(n)
print(f"\nSoma dos dígitos do número fornecido: {soma}")