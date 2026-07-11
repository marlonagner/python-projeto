import banco
import funcoes

banco.criar_tabela()

clientes = []

while True:
 print("\nMenu Inicial:")
 print("1.Cadastrar Cliente")
 print("2. Listar Cliente")
 print("3. Alterar Cliente")
 print("4. Remover Cliente")
 print("5. Buscar Cliente Pelo Nome") #Nova Opcao
 print("6. Sair")

 opcao = input("Escolha uma opcao: ")

 if opcao == "1":
    print("Cadastrar Cliente")
    codigo = input("Digite o codigo do cliente: ")
    nome = input("Digite o nome do cliente: ")

    print (f"Cliente {codigo} - {nome} cadastrado com sucesso!")
    
    #Verificacao para evitar codigos duplicados
    existe = False
    for cliente in clientes:
          if cliente["codigo"] == codigo:
                existe = True
                break
          if existe:
                print(f"Erro: Cliente com codigo {codigo} ja existe!")
          else:
                nome = input("Digite o nome do cliente: ")
                cliente = {"codigo": codigo, "nome": nome}
                clientes.append(cliente)
                print(f"Cliente {codigo} - {nome} cadastrado com sucesso!")
                
 elif opcao == "2":
        print("Listar Clientes")
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
              for cliente in clientes:
                    print(f"Codigo: {cliente['codigo']}, Nome: {cliente['nome']}")



 elif opcao == "3":
        print ("Alterar Clientes")
        codigo = input("Digite o codigo do cliente que deseja alterar: ")

        cliente_encontrado = None 
        for cliente in clientes:
              if cliente["codigo"] == codigo:
                    cliente_encontrado = cliente
                    break

        if cliente_encontrado:
              nome = input("Digite o novo nome do cliente: ")
              cliente_encontrado["nome"] = nome
              print(f"Cliente {codigo} - {nome} alterado com sucesso!")
        else:
              print(f"Cliente com codigo {codigo} nao encontrado.")

 elif opcao == "4":
        print("Remover cliente")
        codigo = input("Digite o codigo do cliente que deseja remover: ")
        
        cliente_encontrado = None
        for cliente in clientes:
              if cliente["codigo"] == codigo:
                    cliente_encontrado = cliente
                    break
        if cliente_encontrado:
              clientes.remove(cliente_encontrado)
              print(f"Cliente {codigo} - {cliente_encontrado['nome']} removido com sucesso!")
        else:
              print(f"Cliente com codigo {codigo} nao encontrado.")

 elif opcao == "5":
        buscar = input("Digiete o código do nome do cliente:")

        cliente_encontrado = None
        for cliente in clientes:
                  if cliente["codigo"] == buscar or cliente["nome"] == buscar:
                        cliente_encontrado = cliente
                        break

        if cliente_encontrado:
          print(f"Cliente encontrado: Codigo: {cliente_encontrado['codigo']}, Nome: {cliente_encontrado['nome']}")
        else:
         print("Erro: Cliente não encontrado.")

 elif opcao == "6":
        print("Saindo do sistema. See Ya!")
        break
 else:
        print("A Opcao escolhida nao existe. Por favor, tente novamente.")