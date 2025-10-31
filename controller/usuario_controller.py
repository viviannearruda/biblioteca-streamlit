from model.usuario_model import Usuario
from service.usuario_service import salvar_usuario, listar_usuarios

def cadastrar_usuario(cpf, nome):
    if not cpf or not nome:
        return "Preencha todos os campos!"
    usuario = Usuario(cpf, nome)
    try:
        salvar_usuario(usuario)
        return f"Usuário '{nome}' cadastrado com sucesso!"
    except Exception as e:
        return f"Erro ao cadastrar: {e}"

def obter_usuarios():
    return listar_usuarios()
