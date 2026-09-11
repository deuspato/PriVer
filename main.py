import os

#Input section
Name = ""

os.system('clear')

#operational menu
while True:
    ultima_linha = ""

    if os.path.exists("logbook"):
        with open("logbook", "r", encoding="utf-8") as arquivo:
            for linha in arquivo:
                ultima_linha = linha
    else:
        print("O arquivo não foi encontrado.")

    # Remove a quebra de linha do final
    ultima_linha = ultima_linha.strip()

    LengCount = len(Name)
    
    listagemLis = ""

    with open("logbook", "r", encoding="utf-8") as listagem:
        listagem = listagemLis
    
    print(f"Ultima linha: {ultima_linha}")
    print(f"Tamanho: {LengCount}")
    print("\n--- MENU ---")
    print("1. Cadastrar usuário")
    print("2. Listar usuários")
    print("3. Configurações")
    print("0. Sair")
    opcao = input("Escolha uma opção: ").strip()

    match opcao:
        case "1":
            print("-> Executando: Cadastro de Usuário...")
            Name = str(input("Please insert a name: "))
        case "2":
            print("-> Executando: Listagem de Usuários...")
            print(listagemLis)
            os.system('clear')
        case "3":
            print("-> Executando: Configurações do Sistema...")
        case "0":
            print("Encerrando o programa. Até logo!")
            break
        case _:  # O caractere '_' funciona como o 'default' (opção inválida)
            print("Opção inválida! Tente novamente.")


#process section
with open("logbook", "a", encoding="utf-8") as arquivo:
    arquivo.write(Name + "\n")
