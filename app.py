while True:
 print("\nMenu Inicial:")
 print("1.Cadastrar Cliente")
 print("2. Listar Cliente")
 print("3. Alterar Cliente")
 print("4. Remover Cliente")
 print("5. Sair")
 opcao = input("Escolha uma opcao: ")

 if opcao == "1":
    print("Cadastrar Cliente")
    codigo = input("Digite o codigo do cliente: ")
    nome = input("Digite o nome do cliente: ")
    print (f"Cliente {codigo} - {nome} cadastrado com sucesso!")
 elif opcao == "2":
        print("Listar Clientes")
 elif opcao == "3":
        print ("Alterar Clientes")
        codigo = input("Digite o codigo do cliente que deseja alterar: ")
        nome=   input("Digite o novo nome do cliente: ")
        print(f"Cliente {codigo} - {nome} alterado com sucesso!")

 elif opcao == "4":
        print("Remover cliente")
        codigo = input("Digite o codigo do cliente que deseja remover: ")
        print (f"Cliente {codigo} removido com sucesso!")
        
 elif opcao == "5":
        print("Saindo do sistema. See Ya!")
        break
 else:
        print("A Opcao escolhida nao existe. Por favor, tente novamente.")