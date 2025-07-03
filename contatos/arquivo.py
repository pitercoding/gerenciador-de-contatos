import os

ARQUIVO = "contatos.txt"

def carregar_contatos():
    contatos = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, 'rt', encoding='utf-8') as f:
            for linha in f:
                try:
                    nome, telefone, email = linha.strip().split(',')
                    contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
                except ValueError:
                    continue  # Ignora linhas inválidas
    return contatos

def salvar_contatos(contatos):
    with open(ARQUIVO, 'wt', encoding='utf-8') as f:
        for c in contatos:
            f.write(f"{c['nome']},{c['telefone']},{c['email']}\n")
