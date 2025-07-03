from time import sleep
from contatos.funcoes import (
    cadastrar_contato,
    listar_contatos,
    buscar_contato,
    remover_contato,
    titulo
)
from contatos.arquivo import carregar_contatos, salvar_contatos

def menu():
    contatos = carregar_contatos()
    while True:
        titulo("GERENCIADOR DE CONTATOS")
        print("1. Cadastrar contato")
        print("2. Listar contatos")
        print("3. Buscar contato")
        print("4. Remover contato")
        print("5. Sair")
        try:
            opcao = int(input("Escolha uma opção: "))
            if opcao == 1:
                titulo("CADASTRO DE CONTATOS")
                cadastrar_contato(contatos)
            elif opcao == 2:
                titulo("LISTA DE CONTATOS")
                listar_contatos(contatos)
            elif opcao == 3:
                titulo("BUSCAR CONTATO")
                buscar_contato(contatos)
            elif opcao == 4:
                titulo("REMOVER CONTATO")
                remover_contato(contatos)
            elif opcao == 5:
                salvar_contatos(contatos)
                print("\033[32mSaindo... Contatos salvos.\033[0m")
                sleep(1)
                print("\033[34mPrograma finalizado. Volte sempre!\033[0m")
                break
            else:
                print("\033[31m[ERRO] Opção inválida.\033[0m")
        except ValueError:
            print("\033[31m[ERRO] Digite um número válido.\033[0m")
