import csv, os

print('''
      [1] Criar uma nova
      [2] Editar um feita
     ''')

tabela = input('Escolha uma opção acima: ')

match tabela:                                ################criar a tabela##################
    case '1':
        print(' ')
        nome_arquivo = input("Qual o nome da nova planilha (ex: tabela.csv): ")

        registros = []
        n1 = int(input('Qual o tamanho da tabela: '))
        contador = 1

        while contador <= n1:
            nome = input('Nome: ')
            idd = int(input('Idade:  '))
            cdd = input('Cidade: ')

            registros.append({
                "Nome": nome, "Idade": idd, "Cidade": cdd,
            })

            contador += 1

        with open(nome_arquivo, "w", newline="", encoding="utf-8") as f:
            campos = ["Nome", "Idade", "Cidade"]
            writer = csv.DictWriter(f, fieldnames=campos)
            writer.writeheader()
            writer.writerows(registros)
            print('Arquivo criado com sucesso!')

    case '2':                             ################ADICIONAR NOME###############################              
        print ('''
      [1] Adicionar um novo nome
      [2] Procurar um nome na planilha   
               ''')
        opcao = input('Escolha uma opção acima: ')
        print('')

        match opcao:
            case '1':
                nome_arquivo = input("Qual o nome da planilha que deseja editar (ex: tabela.csv): ")
                try:
                    with open(nome_arquivo, "a", newline="", encoding="utf-8") as f:
                        campos = ["Nome", "Idade", "Cidade"]
                        writer = csv.DictWriter(f, fieldnames=campos)

                        if os.path.getsize(nome_arquivo) == 0:
                            writer.writeheader()

                        nome = input('Qual nome? ')
                        idd = int(input('Qual idade? '))
                        cdd = input('Qual cidade nasceu? ')

                        writer.writerow({"Nome": nome, "Idade": idd, "Cidade": cdd})
                        print("Registro adicionado com sucesso!")
                except FileNotFoundError:
                    print("Arquivo não encontrado. Crie a tabela primeiro usando a opção [1].")
                
            case "2":                          #########################PROCURAR O NOME###################
                nome_arquivo = input("Qual o nome da planilha que deseja editar (ex: tabela.csv): ")
                nome = input('Qual nome você quer procurar? ')

                try:
                    with open(nome_arquivo, "r", encoding="utf-8") as documento:
                        header = documento.readline().strip().split(",")
                        encontrado = False

                        for linha in documento:
                            if not linha.strip():
                                continue

                        campos = linha.strip().split(",")
                        registro = dict(zip(header, campos))

                        if campos[0].strip().lower() == nome.strip().lower():
                            print("\nRegistro encontrado:")
                        for chave, valor in registro.items():
                            print(f"{chave}: {valor}")
                        encontrado = True

                        if not encontrado:
                            print("Nome não encontrado.")
                except FileNotFoundError:
                    print("Arquivo não encontrado. Verifique o nome da tabela.")

            case _:
                print("Opção inválida")
    case _:
        print("Opção inválida")


        
