#Fazer uma agenda de contatos baseando-se no exemplo fornecido
def criar_contato():
    nome = str(input("\nNome: ")).strip().title() #Essa última função deixa a primeira letra da string fornecida maiúscula!
    telefone = str(input("Telefone: ")).strip()
    email = str(input("E-mail: ")).strip()

    return {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

agenda = {}
while True: #Loop infinito
    comando = str(input("Deseja adicionar um novo contato à agenda? (S/N)\n")).upper().strip()
    if comando == "N":
        break #Sai do loop infinito
    elif comando == "S":
        novo_contato = criar_contato()
        nome_chave = novo_contato["nome"]
        #Agora, verificamos se o nome já está na lista de contatos
        if nome_chave in agenda:
            print("\nErro: já existe um contato com esse nome!")
        else:
            agenda[nome_chave] = novo_contato
            print(f"\nO contato '{nome_chave}' foi salvo com sucesso!")
    else:
        print("\nComando inválido. Por favor, digite 'S' ou 'N'.")

def mostra_agenda(agenda):
    if not agenda:
        print("\nSua agenda está vazia.")
    else:
        print("\nSua agenda de contatos")
        print("-" * 40)
        for nome, dados in agenda.items():
            print(f"{nome}:")
            print(f"- E-mail: {dados['email']}")
            print(f"- Telefone: {dados['telefone']}")
            print("-" * 40)

mostra_agenda(agenda)