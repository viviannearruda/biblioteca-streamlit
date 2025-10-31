from dados.database import conectar_db


def salvar_livro(livro):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO livros (isbn, titulo) VALUES (?, ?)", (livro.isbn, livro.titulo))
    conn.commit()
    conn.close()



def listar_livros():        
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("SELECT isbn, titulo FROM livros")
    livros = cursor.fetchall()
    conn.close()
    return livros 