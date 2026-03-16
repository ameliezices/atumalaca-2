#Programa que lê dois vetores, com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores

print("Digite os 10 elementos do primeiro vetor")
vetor1 = []
for i in range(10):
    elemento = float(input(f"Elemento {i + 1}: "))
    vetor1.append(elemento)

print("\nDigite os 10 elementos do segundo vetor")
vetor2 = []
for i in range(10):
    elemento = float(input(f"Elemento {i + 1}: "))
    vetor2.append(elemento)

vetor3 = []
for i in range(10):
    vetor3.append(vetor1[i])
    vetor3.append(vetor2[i])

print("\nTerceiro vetor:")
print(vetor3)