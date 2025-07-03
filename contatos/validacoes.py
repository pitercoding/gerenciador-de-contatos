def validar_nome(nome):
    partes = nome.strip().split()
    return bool(partes) and all(palavra.isalpha() for palavra in partes)

def validar_telefone(telefone):
    return telefone.isdigit()

def validar_email(email):
    return '@' in email and '.' in email and ' ' not in email
