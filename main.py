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
        caminho = input("Digite o caminho do arquivo (ex: peca.stl): ")

        try:
            if caminho != "":
                registroFile["caminho_origem"] = caminho

                # Extrai nome e extensão usando fatiamento direto
                pos_barra = caminho.rfind("/")
                if pos_barra != -1:
                    nome_completo = caminho[pos_barra + 1 :]
                else:
                    nome_completo = caminho

                pos_ponto = nome_completo.rfind(".")
                if pos_ponto != -1:
                    registroFile["nome_base"] = nome_completo[:pos_ponto]
                    registroFile["extensao"] = nome_completo[pos_ponto:]
                else:
                    registroFile["nome_base"] = nome_completo
                    registroFile["extensao"] = ""

                # Operadores de incremento direto nas chaves
                registroFile["qtd_envios"] += 1
                registroFile["versao"] += 1
                registroFile["ultimo_arquivo_salvo"] = (
                    f"v{registroFile['versao']}_{registroFile['nome_base']}{registroFile['extensao']}"
                )

                # Copia física dos bytes do arquivo 
                arq_leitura = open(registroFile["caminho_origem"], "rb")
                conteudo = arq_leitura.read()
                arq_leitura.close()
                
                arq_escrita = open(registroFile["ultimo_arquivo_salvo"], "wb")
                arq_escrita.write(conteudo)
                arq_escrita.close()

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
                f"Versão: v{registroFile['versao']} | Envios: {registroFile['qtd_envios']} | Arquivo: {registroFile['ultimo_arquivo_salvo']}"
            )
        else:
            print("Nenhum arquivo enviado até o momento.")

    elif opcao == "3":
        clear_screen()
        if registroFile["registro_ativo"]:
            novo_nome = input("Digite o novo nome base: ")
            if novo_nome != "":
                registroFile["nome_base"] = novo_nome
                print(
                    f"Próximas versões serão salvas como: v{registroFile['versao'] + 1}_{registroFile['nome_base']}{registroFile['extensao']}"
                )
        else:
            print("Envie um arquivo antes de atualizar.")

    elif opcao == "4":
        clear_screen()
        # O template brilha aqui: restaura tudo para o padrão em uma linha!
        registroFile = templateFile.copy()
        print("Registros zerados com sucesso.")

    elif opcao == "5":
        registroFile["executando"] = False
        print("Encerrando o programa.")
        clear_screen()

    else:
        clear_screen()
        print("Opção inválida.")