import streamlit as st
from controller.livro_controller import cadastrar_livro, obter_livros
from controller.usuario_controller import cadastrar_usuario, obter_usuarios
from controller.emprestimo_controller import cadastrar_emprestimo, obter_emprestimos
from dados.database import criar_tabelas

criar_tabelas()

st.title("Sistema da Biblioteca")

menu = st.sidebar.radio("Escolha uma seção:", ["Livros", "Usuários", "Empréstimos"])

# ====================== LIVROS ======================
if menu == "Livros":
    st.header("Cadastro de Livros")
    with st.form("form_livro"):
        isbn = st.text_input("ISBN")
        titulo = st.text_input("Título")
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            mensagem = cadastrar_livro(isbn, titulo)
            st.success(mensagem)

    st.subheader("Livros cadastrados")
    livros = obter_livros()
    if livros:
        for l in livros:
            st.write(f"**ISBN:** {l[0]} | **Título:** {l[1]}")
    else:
        st.info("Nenhum livro cadastrado ainda")

# ====================== USUÁRIOS ======================
elif menu == "Usuários":
    st.header("Cadastro de Usuários")
    with st.form("form_usuario"):
        cpf = st.text_input("CPF")
        nome = st.text_input("Nome")
        submitted = st.form_submit_button("Cadastrar")

        if submitted:
            mensagem = cadastrar_usuario(cpf, nome)
            st.success(mensagem)

    st.subheader("Usuários cadastrados")
    usuarios = obter_usuarios()
    if usuarios:
        for u in usuarios:
            st.write(f"**CPF:** {u[0]} | **Nome:** {u[1]}")
    else:
        st.info("Nenhum usuário cadastrado ainda")

# ====================== EMPRÉSTIMOS ======================
elif menu == "Empréstimos":
    st.header("Registrar Empréstimo")

    usuarios = obter_usuarios()
    livros = obter_livros()

    if not usuarios or not livros:
        st.warning("Cadastre pelo menos um usuário e um livro antes de registrar empréstimos.")
    else:
        with st.form("form_emprestimo"):
            cpf_usuario = st.selectbox("Usuário", [u[0] + " - " + u[1] for u in usuarios])
            isbn_livro = st.selectbox("Livro", [l[0] + " - " + l[1] for l in livros])
            submitted = st.form_submit_button("Registrar Empréstimo")

            if submitted:
                cpf = cpf_usuario.split(" - ")[0]
                isbn = isbn_livro.split(" - ")[0]
                mensagem = cadastrar_emprestimo(cpf, isbn)
                st.success(mensagem)

    st.subheader("Empréstimos registrados")
    emprestimos = obter_emprestimos()

    if emprestimos:
        for e in emprestimos:
            st.write(f"**Usuário:** {e[1]} | **Livro:** {e[2]} | **Data:** {e[3]}")
    else:
        st.info("Nenhum empréstimo registrado ainda.")
