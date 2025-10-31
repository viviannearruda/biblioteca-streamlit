from datetime import datetime

class Emprestimo:
    def __init__(self, cpf_usuario: str, isbn_livro: str, data_emprestimo: str = None):
        self.cpf_usuario = cpf_usuario
        self.isbn_livro = isbn_livro
        self.data_emprestimo = data_emprestimo or datetime.now().strftime("%d/%m/%Y %H:%M")
