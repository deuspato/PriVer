import os

templateFile = {
    "caminho_origem": "",
    "nome_base": "",
    "extensao": "",
    "qtd_envios": 0,
    "versao": 0,
    "ultimo_arquivo_salvo": "",
    "registro_ativo": False,
    "executando": True,
}

registroFile = templateFile.copy()


def clear_screen():
    os.system("cls") if os.name == "nt" else os.system("clear")


clear_screen()
while registroFile["executando"]:
    print("\n--- VERSIONADOR 3D (SEM FUNÇÕES) ---")
    print("1. Enviar arquivo real (Gera nova versão v1, v2...)")
    print("2. Consultar versão atual")
    print("3. Atualizar nome base")
    print("4. Resetar / Deletar")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        clear_screen()
        caminho = input("Digite o caminho do arquivo (ex: C:\\pasta\\peca.stl): ").strip("\"' ")

        try:
            if caminho != "":
                caminho_normalizado = os.path.normpath(caminho)
                registroFile["caminho_origem"] = caminho_normalizado

                nome_completo = os.path.basename(caminho_normalizado)
                nome_base, extensao = os.path.splitext(nome_completo)

                if not registroFile["registro_ativo"]:
                    registroFile["nome_base"] = nome_base

                registroFile["extensao"] = extensao

                with open(registroFile["caminho_origem"], "rb") as arq_leitura:
                    conteudo = arq_leitura.read()

                registroFile["qtd_envios"] += 1
                registroFile["versao"] += 1
                registroFile["ultimo_arquivo_salvo"] = (
                    f"v{registroFile['versao']}_{registroFile['nome_base']}{registroFile['extensao']}"
                )

                with open(registroFile["ultimo_arquivo_salvo"], "wb") as arq_escrita:
                    arq_escrita.write(conteudo)

                registroFile["registro_ativo"] = True
                print(
                    f"Arquivo copiado como: {registroFile['ultimo_arquivo_salvo']} (Envios: {registroFile['qtd_envios']})"
                )
                print("Estado atual do dicionário:", registroFile)
            else:
                clear_screen()
                print("Caminho não pode ser vazio.")
        except FileNotFoundError:
            clear_screen()
            print(f"Erro: O arquivo '{caminho}' não existe.")
        except PermissionError:
            clear_screen()
            print(f"Erro: Sem permissão para ler o arquivo '{caminho}'.")

    elif opcao == "2":
        clear_screen()
        if registroFile["registro_ativo"]:
            print(
                f"Versão: v{registroFile['versao']} | Envios: {registroFile['qtd_envios']} | "
                f"Nome base atual: {registroFile['nome_base']} | Arquivo atual: {registroFile['ultimo_arquivo_salvo']}"
            )
        else:
            print("Nenhum arquivo enviado até o momento.")

    elif opcao == "3":
        clear_screen()
        if registroFile["registro_ativo"]:
            novo_nome = input("Digite o novo nome base: ").strip()
            if novo_nome != "":
                arquivo_antigo = registroFile["ultimo_arquivo_salvo"]
                novo_arquivo = f"v{registroFile['versao']}_{novo_nome}{registroFile['extensao']}"

                if os.path.isfile(arquivo_antigo) and arquivo_antigo != novo_arquivo:
                    os.rename(arquivo_antigo, novo_arquivo)

                registroFile["nome_base"] = novo_nome
                registroFile["ultimo_arquivo_salvo"] = novo_arquivo

                print(f"Nome base atualizado! Arquivo atual renomeado para: {registroFile['ultimo_arquivo_salvo']}")
        else:
            print("Envie um arquivo antes de atualizar.")

    elif opcao == "4":
        clear_screen()
        registroFile = templateFile.copy()
        print("Registros zerados com sucesso.")

    elif opcao == "5":
        registroFile["executando"] = False
        print("Encerrando o programa.")
        clear_screen()

    else:
        clear_screen()
        print("Opção inválida.")