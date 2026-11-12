import os

# Variáveis simples de controle (sem listas nem funções)
caminho_origem = ""
nome_base = ""
extensao = ""
qtd_envios = 0
versao = 0
ultimo_arquivo_salvo = ""
registro_ativo = False
executando = True

os.system("clear")
while executando:
    print("\n--- VERSIONADOR 3D (SEM FUNÇÕES) ---")
    print("1. Enviar arquivo real (Gera nova versão v1, v2...)")
    print("2. Consultar versão atual")
    print("3. Atualizar nome base")
    print("4. Resetar / Deletar")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        os.system("clear")
        caminho_origem = input("Digite o caminho do arquivo (ex: peca.stl): ")

        if caminho_origem != "":
            # Extrai nome e extensão usando fatiamento direto (sem funções prontas de split)
            pos_barra = caminho_origem.rfind("/")
            if pos_barra != -1:
                nome_completo = caminho_origem[pos_barra + 1 :]
            else:
                nome_completo = caminho_origem

            pos_ponto = nome_completo.rfind(".")
            if pos_ponto != -1:
                nome_base = nome_completo[:pos_ponto]
                extensao = nome_completo[pos_ponto:]
            else:
                nome_base = nome_completo
                extensao = ""

            # Operadores de incremento
            qtd_envios = qtd_envios + 1
            versao = versao + 1
            ultimo_arquivo_salvo = f"v{versao}_{nome_base}{extensao}"

            # Copia física dos bytes do arquivo
            arq_leitura = open(caminho_origem, "rb")
            conteudo = arq_leitura.read()
            arq_leitura.close()

            arq_escrita = open(ultimo_arquivo_salvo, "wb")
            arq_escrita.write(conteudo)
            arq_escrita.close()

            registro_ativo = True
            print(f"Arquivo copiado como: {ultimo_arquivo_salvo} (Envios: {qtd_envios})")
        else:
            print("Caminho não pode ser vazio.")

    elif opcao == "2":
        os.system("clear")
        if registro_ativo:
            print(f"Versão: v{versao} | Envios: {qtd_envios} | Arquivo: {ultimo_arquivo_salvo}")
        else:
            print("Nenhum arquivo enviado até o momento.")

    elif opcao == "3":
        os.system("clear")
        if registro_ativo:
            novo_nome = input("Digite o novo nome base: ")
            if novo_nome != "":
                nome_base = novo_nome
                print(f"Próximas versões serão salvas como: v{versao + 1}_{nome_base}{extensao}")
        else:
            print("Envie um arquivo antes de atualizar.")

    elif opcao == "4":
        os.system("clear")
        caminho_origem = ""
        nome_base = ""
        extensao = ""
        qtd_envios = 0
        versao = 0
        ultimo_arquivo_salvo = ""
        registro_ativo = False
        print("Registros zerados com sucesso.")

    elif opcao == "5":
        executando = False
        print("Encerrando o programa.")
        os.system("clear")

    else:
        print("Opção inválida.")
        os.system("clear")