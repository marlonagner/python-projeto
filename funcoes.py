import sqlite3

def cadastrar_cliente(codigo, nome):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    try:
        cursor.execute("INSERT INTO clientes (codigo, nome) VALUES (?, ?)", (codigo, nome))
        conexao.commit()
        print(f"Cliente {codigo} - {nome} cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print(f"Erro: Cliente com codigo {codigo} ja existe.")
    finally:
        conexao.close()

def listar_clientes():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT codigo, nome FROM clientes")
    clientes = cursor.fetchall()
    conexao.close()

    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        print("\nLista de Clientes:")
        for codigo, nome in clientes:
         print(f"Código : {codigo}, Nome: {nome} ")

def alterar_cliente(codigo, novo_nome):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("UPDATE clientes SET nome = ? WHERE codigo = ?", (novo_nome, codigo))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Cliente {codigo} - {novo_nome} alterado com sucesso!")
    else:
        print(f"Cliente com codigo {codigo} nao encontrado.")   

    conexao.close()
   
def remover_cliente(codigo):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM clientes WHERE codigo = ?", (codigo,))
    conexao.commit()

    if cursor.rowcount > 0:
        print(f"Cliente {codigo} removido com sucesso!")
    else:
        print(f"Cliente com codigo {codigo} nao encontrado.")
     
    conexao.close()

def buscar_cliente(termo):
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()
    cursor.execute("SELECT codigo, nome FROM clientes WHERE codigo = ? OR nome LIKE ?", (termo, f"%{termo}%"))
    clientes = cursor.fetchall()
    conexao.close()

    if clientes:
     print("\nClientes encontrados:")
    for codigo, nome in clientes:
        print(f"Código: {codigo}, Nome: {nome}")
    else:
        print("Erro: Cliente não encontrado.")
