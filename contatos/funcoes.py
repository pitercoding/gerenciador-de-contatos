from contatos.validacoes import validar_nome, validar_telefone, validar_email

def titulo(texto):
    print('-' * 30)
    print(f'{texto:^30}')
    print('-' * 30)

def cadastrar_contato(contatos):
    while True:
        nome = input("Nome: ").strip()
        if validar_nome(nome):
            break
        print("\033[31mNome inválido. Use apenas letras e espaços.\033[0m")

    while True:
        telefone = input("Telefone (somente números): ").strip()
        if validar_telefone(telefone):
            break
        print("\033[31mTelefone inválido. Use apenas números.\033[0m")

    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            break
        print("\033[31mEmail inválido. Use um formato válido (ex: nome@email.com).\033[0m")

    contatos.append({'nome': nome, 'telefone': telefone, 'email': email})
    print("\033[33mContato adicionado com sucesso!\033[0m")

def listar_contatos(contatos):
    if not contatos:
        print("\033[31mNenhum contato cadastrado.\033[0m")
    else:
        for i, c in enumerate(contatos, 1):
            print(f"{i}. Nome: {c['nome']} - Telefone: {c['telefone']} - Email: {c['email']}")

def buscar_contato(contatos):
    termo = input("Buscar por nome: ").lower()
    resultados = [c for c in contatos if termo in c['nome'].lower()]
    if resultados:
        for c in resultados:
            print(f"{c['nome']} - {c['telefone']} - {c['email']}")
    else:
        print("\033[31mNenhum contato encontrado com esse nome.\033[0m")

def remover_contato(contatos):
    termo = input("Remover por nome: ").lower()
    resultados = [c for c in contatos if termo in c['nome'].lower()]

    if not resultados:
        print("\033[31mNenhum contato encontrado para remover.\033[0m")
        return

    for i, c in enumerate(resultados, 1):
        print(f"{i}. {c['nome']} - {c['telefone']} - {c['email']}")

    try:
        escolha = int(input("Digite o número do contato a remover: "))
        if 1 <= escolha <= len(resultados):
            contatos.remove(resultados[escolha - 1])
            print("\033[32mContato removido com sucesso.\033[0m")
        else:
            print("\033[31mNúmero inválido.\033[0m")
    except ValueError:
        print("\033[31mEntrada inválida. Digite um número.\033[0m")
