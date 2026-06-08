#Programa que recebe uma string e retorne um dicionário com a frequência de cada palavra, bem como a palavra mais frequente e sua quantidade
import string

def tira_pontuacao(texto):
    texto_limpo = ""
    for caractere in texto:
        if caractere not in string.punctuation:
            texto_limpo += caractere
    return texto_limpo

def verifica_frequencia(texto):
    texto = tira_pontuacao(texto).lower()
    palavras = texto.split()
    frequencia = {}
    for palavra in palavras:
        frequencia[palavra] = frequencia.get(palavra, 0) + 1 #Pega o valor atual da chave ou atribui 0 se não existir, e soma 1!
        #A função .get(nome_da_chave, valor_padrao_dela) é usada para acessar o valor de uma chave específica em um dicionário. Note que o campo da variável valor_padrao_dela é opcional para preenchimento
    palavra_mais_frequente = max(frequencia, key = frequencia.get)
    quant_palavra_mais_freq = frequencia[palavra_mais_frequente]
    dic_ordenado = dict(sorted(frequencia.items(), key = lambda item: item[1], reverse = True))
    return dic_ordenado, palavra_mais_frequente, quant_palavra_mais_freq

texto = str(input("Insira um texto:\n"))
frequencias, palavra_mais_frequente, quantidade = verifica_frequencia(texto)
print(f"\nFrequência de cada palavra: {frequencias}")
print(f"Palavra mais frequente: {palavra_mais_frequente} ({quantidade} ocorrências)")