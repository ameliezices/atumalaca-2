#Função que recebe dois números e retorna True se o primeiro for múltiplo do segundo
def multiplo(a, b):
    if a % b == 0:
        return True
    else:
        return False

primeiro = float(input("Insire o primeiro valor: "))
segundo = float(input("Insire o segundo valor: "))
verificacao = multiplo(primeiro, segundo)
if verificacao:
    print(f"\nSim, {primeiro} é múltiplo de {segundo}")
else:
    print(f"\nNão, {primeiro} não é múltiplo de {segundo}")