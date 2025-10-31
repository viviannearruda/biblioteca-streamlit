from dados.database import conectar_db

def salvar_emprestimo(emprestimo):
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO emprestimos (cpf_usuario, isbn_livro, data_emprestimo)
        VALUES (?, ?, ?)
    """, (emprestimo.cpf_usuario, emprestimo.isbn_livro, emprestimo.data_emprestimo))
    conn.commit()
    conn.close()


def listar_emprestimos():
    conn = conectar_db()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT e.id, u.nome, l.titulo, e.data_emprestimo
        FROM emprestimos e
        JOIN usuarios u ON e.cpf_usuario = u.cpf
        JOIN livros l ON e.isbn_livro = l.isbn
    """)
    emprestimos = cursor.fetchall()
    conn.close()
    return emprestimos
