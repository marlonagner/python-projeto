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