#Programa que lê o números de palavras em um texto

texto = input("Forneça um texto: ")

palavras = texto.split()
quantidade = len(palavras)

print(f"\nQuantidade de palavras: {quantidade}")