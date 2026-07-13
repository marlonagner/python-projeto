import sqlite3

def criar_tabela():
    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes(
            codigo TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS enderecos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_codigo TEXT,
            rua TEXT,
            numero TEXT,
            cidade TEXT,
            FOREIGN KEY(cliente_codigo) REFERENCES clientes(codigo)
        )
    """)

    conexao.commit()
    conexao.close()

    print("Banco de dados e tabelas criados com sucesso!")