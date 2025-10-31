# 📚 Biblioteca Streamlit

## ✨ Descrição do Projeto
Este é um projeto de **empréstimo de livros para usuários de uma biblioteca**, desenvolvido com foco na **visualização interativa** e facilidade de uso.  

O projeto utiliza:  
- 💻 **Streamlit**: para criar a interface visual.  
- 🛠️ **venv (ambiente virtual)**: para gerenciar dependências do Python de forma isolada.  

---

## 🚀 Funcionalidades
- 👤 **Cadastro e visualização de usuários**  
- 📖 **Cadastro e visualização de livros**  
- 🔄 **Registro de empréstimos de livros**  
- 🖥️ **Interface amigável e interativa** com Streamlit




### 2️⃣ **Criar e ativar o ambiente virtual:**

python -m venv venv

### **Windows (PowerShell)**
.\venv\Scripts\Activate

### **Instalar dependências:**
pip install streamlit

### **Rodar a aplicação:**
streamlit run app.py

### 📂 **Estrutura do Projeto**
biblioteca-streamlit/
│
├─ controller/
│   ├─ emprestimo_controller.py
│   ├─ livro_controller.py
│   └─ usuario_controller.py
│
├─ dados/
│   └─ database.py
│
├─ model/
│   ├─ emprestimo_model.py
│   ├─ livro_model.py
│   └─ usuario_model.py
│
├─ service/
│   ├─ emprestimo_service.py
│   ├─ livro_service.py
│   └─ usuario_service.py
│
├─ venv/   (ambiente virtual, não versionado)
└─ app.py

### 👩‍💻 **Autor**

**Vivianne Renatta Melo de Arruda**
