import sqlite3

#Conectar ao banco de dados ou criar caso não exista

conexao =sqlite3.connect("clientes.db   ")
cursor = conexao.cursor()

# criar tabela de clientes
cursor.execute('''CREATE TABLE IF NOT EXISTS clientes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               codigo TEXT UNIQUE NOT NULL,
               nome TEXT NOT NULL
               )
               ''')
print("Banco de dados e tabela criados com sucesso!")
#fechar conexao
conexao.close()

#criar tabela de endereços
cursor.execute("""
               CREATE TABLE IF NOT EXISTS enderecos(
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               cliente_codigo TXT,
               rua TEXT NOT NULL,
               cidade TEXT NOT NULL,
               FOREIGN KEY (cliente_codigo) REFERENCES clientes(codigo)
               )
               """)
conexao.commit()
conexao.close()
