from model.emprestimo_model import Emprestimo
from service.emprestimo_service import salvar_emprestimo, listar_emprestimos

def cadastrar_emprestimo(cpf_usuario, isbn_livro):
    if not cpf_usuario or not isbn_livro:
        return "Preencha todos os campos!"
    emprestimo = Emprestimo(cpf_usuario, isbn_livro)
    try:
        salvar_emprestimo(emprestimo)
        return "Empréstimo registrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar empréstimo: {e}"

def obter_emprestimos():
    return listar_emprestimos()
