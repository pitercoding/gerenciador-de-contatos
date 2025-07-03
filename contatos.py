# contatos.py

import os

ARQUIVO = "contatos.txt"

def carregar_contatos():
    contatos = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'rt', encoding='utf-8') as f:
            for linha in f:
                nome, telefone, email = linha.strip().split(',')
                contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
    return contatos

def salvar_contatos(contatos):
    with open(ARQUIVO, 'wt', encoding='utf-8') as f:
        for c in contatos:
            f.write(f"{c['nome']},{c['telefone']},{c['email']}\n")

def cadastrar_contato(contatos):
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("Email: ")
    contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
    print("\033[33mContato adicionado com sucesso!\033[0m")

def listar_contatos(contatos):
    if not contatos:
        print("\033[31mNenhum contato cadastrado.\033[0m")
    for i, c in enumerate(contatos, 1):
        print(f"{i}. Nome: {c['nome']} - Telefone: {c['telefone']} - Email: {c['email']}")

def buscar_contato(contatos):
    termo = input("Buscar por nome: ").lower()
    resultados = [c for c in contatos if termo in c['nome'].lower()]
    for c in resultados:
        print(f"{c['nome']} - {c['telefone']} - {c['email']}")
    if not resultados:
        print("\033[31mNenhum contato encontrado com esse nome.\033[0m")

def menu():
    contatos = carregar_contatos()
    while True:
        print("\n1. Cadastrar contato\n2. Listar contatos\n3. Buscar contato\n4. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                cadastrar_contato(contatos)
            elif opcao == 2:
                listar_contatos(contatos)
            elif opcao == 3:
                buscar_contato(contatos)
            elif opcao == 4:
                salvar_contatos(contatos)
                print("\033[34mFinalizando programa... Volte sempre!\033[0m")
                break
            else:
                print("\033[31m[ERRO] Opção inválida.\033[0m")
        except ValueError:
            print("\033[31m[ERRO] Digite um número válido.\033[0m")

if __name__ == "__main__":
    menu()

