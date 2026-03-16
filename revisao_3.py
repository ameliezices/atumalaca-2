#Programa que imprime uma matriz 3x4 em que cada posição seja dada por i * j

for i in range(1, 4):
    for j in range(1, 5):
        valor = i * j
        print(f"{valor:4}", end="") #Mostra os elementos [i][j] de forma a reservar 4 espaços para cada um deles. O comando end="" evita que o print pule para outro i até que todos os valores j tenham sido lidos
    print() #Pula a linha quando todos os valores j forem lidos em uma valor i