import sqlite3

DB_name = "livros.db"

def criar_tabelas():
    conn = sqlite3.connect(DB_name)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS livros (
        isbn TEXT PRIMARY KEY,
        titulo TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        cpf TEXT PRIMARY KEY,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS emprestimos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        cpf_usuario TEXT NOT NULL,
        isbn_livro TEXT NOT NULL,
        data_emprestimo TEXT NOT NULL,
        FOREIGN KEY (cpf_usuario) REFERENCES usuarios(cpf),
        FOREIGN KEY (isbn_livro) REFERENCES livros(isbn)
    )
    """)

    conn.commit()
    conn.close()


def conectar_db():
    return sqlite3.connect(DB_name)
