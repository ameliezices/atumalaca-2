#Programa que simula um cadastro de alunos
def cadastra_aluno(cadastro, nome):
    aluno = {}
    aluno["Nome"] = nome
    aluno["Notas"] = []
    cadastro.append(aluno)

def exclui_aluno_cadastrado(cadastro, nome):
    for aluno in cadastro:
        if aluno["Nome"] == nome:
            cadastro.remove(aluno)
            return

def cadastra_nota(cadastro, nome, notas):
    for aluno in cadastro:
        if aluno["Nome"] == nome:
            aluno["Notas"] += notas.split()
            return

def mostra_alunos(cadastro):
    for aluno in cadastro:
        for chave in aluno:
            print(f"{chave}: {aluno[chave]}")

def menu_operacoes(cadastro):
    while True:
        print("\nEscolha uma opção:\n1. Incluir aluno\n2. Excluir aluno\n3. Inserir notas\n4. Exibir turma\n5. Sair\n")
        opcao = int(input())
        if opcao == 1:
            nome = input("Digite o nome do aluno: ")


cadastro = []