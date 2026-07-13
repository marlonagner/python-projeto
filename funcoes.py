import sqlite3


# ==========================================
# Função para cadastrar cliente e endereço
# ==========================================
def cadastrar_cliente(codigo, nome, rua=None, numero=None, cidade=None):

    # Validação dos campos obrigatórios
    if not codigo or not codigo.strip():
        print("Erro: O código do cliente não pode estar vazio.")
        return

    if not nome or not nome.strip():
        print("Erro: O nome do cliente não pode estar vazio.")
        return

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    try:
        # Insere cliente
        cursor.execute(
            "INSERT INTO clientes (codigo, nome) VALUES (?, ?)",
            (codigo.strip(), nome.strip())
        )

        # Insere endereço, se informado
        if rua and numero and cidade:
            cursor.execute(
                """
                INSERT INTO enderecos
                (cliente_codigo, rua, numero, cidade)
                VALUES (?, ?, ?, ?)
                """,
                (
                    codigo.strip(),
                    rua.strip(),
                    str(numero).strip(),
                    cidade.strip()
                )
            )

        conexao.commit()
        print(f"Cliente {codigo} - {nome} cadastrado com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: Já existe um cliente com esse código.")

    finally:
        conexao.close()


# ==========================================
# Listar clientes
# ==========================================
def listar_clientes():

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            c.codigo,
            c.nome,
            e.rua,
            e.numero,
            e.cidade
        FROM clientes c
        LEFT JOIN enderecos e
            ON c.codigo = e.cliente_codigo
    """)

    clientes = cursor.fetchall()
    conexao.close()

    if not clientes:
        print("Nenhum cliente cadastrado.")
        return

    print("\nLista de Clientes:\n")

    for codigo, nome, rua, numero, cidade in clientes:

        if rua:
            endereco = f"{rua}, {numero} - {cidade}"
        else:
            endereco = "Endereço não cadastrado"

        print(f"Código: {codigo}")
        print(f"Nome: {nome}")
        print(f"Endereço: {endereco}")
        print("-" * 40)


# ==========================================
# Alterar cliente
# ==========================================
def alterar_cliente(codigo, novo_nome=None, rua=None, numero=None, cidade=None):

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    try:

        # Verifica se existe
        cursor.execute(
            "SELECT codigo, nome FROM clientes WHERE codigo = ?",
            (codigo,)
        )

        cliente = cursor.fetchone()

        if not cliente:
            print(f"Erro: Cliente com código {codigo} não encontrado.")
            return

        cliente_codigo, nome_atual = cliente

        # Mantém nome atual se não informar outro
        if novo_nome and novo_nome.strip():
            novo_nome = novo_nome.strip()
        else:
            novo_nome = nome_atual

        cursor.execute(
            "UPDATE clientes SET nome = ? WHERE codigo = ?",
            (novo_nome, cliente_codigo)
        )

        # Verifica se já existe endereço
        cursor.execute(
            "SELECT id FROM enderecos WHERE cliente_codigo = ?",
            (cliente_codigo,)
        )

        endereco = cursor.fetchone()

        if endereco:

            cursor.execute("""
                UPDATE enderecos
                SET
                    rua = COALESCE(?, rua),
                    numero = COALESCE(?, numero),
                    cidade = COALESCE(?, cidade)
                WHERE cliente_codigo = ?
            """, (
                rua,
                numero,
                cidade,
                cliente_codigo
            ))

        else:

            if rua and numero and cidade:

                cursor.execute("""
                    INSERT INTO enderecos
                    (cliente_codigo, rua, numero, cidade)
                    VALUES (?, ?, ?, ?)
                """, (
                    cliente_codigo,
                    rua,
                    str(numero),
                    cidade
                ))

            elif rua or numero or cidade:

                print("Aviso: Para cadastrar um novo endereço informe rua, número e cidade.")

        conexao.commit()
        print("Cliente alterado com sucesso!")

    finally:
        conexao.close()

        # ==========================================
# Remover cliente
# ==========================================
def remover_cliente(codigo):

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    try:
        # Remove primeiro o endereço
        cursor.execute(
            "DELETE FROM enderecos WHERE cliente_codigo = ?",
            (codigo,)
        )

        # Remove o cliente
        cursor.execute(
            "DELETE FROM clientes WHERE codigo = ?",
            (codigo,)
        )

        if cursor.rowcount > 0:
            print(f"Cliente {codigo} removido com sucesso!")
        else:
            print(f"Erro: Cliente com código {codigo} não encontrado.")

        conexao.commit()

    finally:
        conexao.close()


# ==========================================
# Buscar cliente
# ==========================================
def buscar_cliente(termo):

    conexao = sqlite3.connect("clientes.db")
    cursor = conexao.cursor()

    cursor.execute("""
        SELECT
            c.codigo,
            c.nome,
            e.rua,
            e.numero,
            e.cidade
        FROM clientes c
        LEFT JOIN enderecos e
            ON c.codigo = e.cliente_codigo
        WHERE c.codigo = ? OR c.nome LIKE ?
    """, (termo, f"%{termo}%"))

    clientes = cursor.fetchall()
    conexao.close()

    if clientes:
        print("\nClientes encontrados:\n")

        for codigo, nome, rua, numero, cidade in clientes:

            if rua and numero and cidade:
                endereco = f"{rua}, {numero} - {cidade}"
            else:
                endereco = "Endereço não cadastrado"

            print(f"Código: {codigo}")
            print(f"Nome: {nome}")
            print(f"Endereço: {endereco}")
            print("-" * 40)

    else:
        print(f"Nenhum cliente encontrado com o termo '{termo}'.")