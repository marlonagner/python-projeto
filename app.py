while True:
 print("\nMenu Inicial:")
 print("1.Cadastrar Cliente")
 print("2. Listar Cliente")
 print("3. Alterar Cliente")
 print("4. Remover Cliente")
 print("5. Sair")
 opcao = input("Escolha uma opcao: ")

 if opcao == "1":
    print("Opcao de Cadastrar Cliente selecionada.")
 elif opcao == "2":
        print("Opcao de Listar Clientes selecionada.")
 elif opcao == "3":
        print ("Opcao de Alterar Clientes selecionados")
 elif opcao == "4":
        print("Opcao de Remover clientes selecionada")
 elif opcao == "5":
        print("Saindo do sistema. See Ya!")
        break
 else:
        print("A Opcao escolhida nao existe. Por favor, tente novamente.")