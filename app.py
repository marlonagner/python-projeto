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
 print("0. Sair")

 opcao = input("Escolha uma opcao: ")

 if opcao == "1":
    print("\nCadastrar Cliente")
    codigo = input("Digite o codigo do cliente: ")
    nome = input("Digite o nome do cliente: ")
    funcoes.cadastrar_cliente(codigo, nome)

   
                
 elif opcao == "2":
        print("Listar Clientes")
        funcoes.listar_clientes()



 elif opcao == "3":
        print ("\nAlterar Cliente\n")
        codigo = input("Digite o codigo do cliente que deseja alterar: ")
        novo_nome = input("Digite o novo nome do cliente: ")
        funcoes.alterar_cliente(codigo, novo_nome)

       

 elif opcao == "4":
        print("\nRemover cliente\n")
        codigo = input("Digite o codigo do cliente que deseja remover: ")
        funcoes.remover_cliente(codigo)
        
      

 elif opcao == "5":
       print("\nBuscar Cliente\n")
       termo = input("Digite o codigo ou nome do cliente que deseja buscar: ")
       funcoes.buscar_cliente(termo)
 

 elif opcao == "0":
        print("Saindo do sistema. See Ya!")
        break
 else:
        print("A Opcao escolhida nao existe. Por favor, tente novamente.")