# OrganizeMe

OrganizeMe é um sistema de gerenciamento de tarefas que permite aos usuários registrar, visualizar, editar e excluir tarefas. O sistema é desenvolvido em Python usando o framework Flask e utiliza um banco de dados MySQL para armazenamento de dados.

## Funcionalidades

- **Registro de Usuário:** Usuários podem se registrar criando uma conta com nome, email e senha.
- **Login e Logout:** Os usuários podem fazer login em suas contas e sair quando desejarem.
- **Gerenciamento de Tarefas:**
  - Adicionar novas tarefas com título, descrição, data limite, status, prioridade e categoria.
  - Listar todas as tarefas associadas ao usuário.
  - Editar detalhes de tarefas existentes.
  - Excluir tarefas indesejadas.

## Tecnologias Utilizadas

- **Backend:**
  - Python
  - Flask
  - Werkzeug (para hash de senhas)
  - mysql-connector (para conexão com o MySQL)
  
- **Banco de Dados:**
  - MySQL
  
- **Frontend:**
  - HTML
  - CSS

## Pré-requisitos

Antes de executar o projeto, você precisa ter o seguinte instalado em sua máquina:

- [Python](https://www.python.org/downloads/) (versão 3.6 ou superior)
- [MySQL](https://dev.mysql.com/downloads/mysql/)
- [XAMPP](https://www.apachefriends.org/index.html) (opcional, para um ambiente de desenvolvimento local)

## Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/fleabagreact/OrganizeMe.git
   cd OrganizeMe
   ```

2. Instale as dependências necessárias:
   ```bash
   pip install -rrequirements.txt
   ```

3. Crie o banco de dados:
   - Execute o arquivo `init_db.py` para criar o banco de dados e as tabelas necessárias:
   ```bash
   python init_db.py
   ```

4. Inicie o servidor Flask:
   ```bash
   python app.py
   ```

5. Acesse o aplicativo em seu navegador:
   ```
   http://127.0.0.1:5000
   ```

## Estrutura do Projeto

```
OrganizeMe/
│
├── app.py               # Arquivo principal da aplicação
├── init_db.py           # Script para inicializar o banco de dados
├── models.py            # Modelos para interação com o banco de dados
├── templates/           # Diretório para templates HTML
│   ├── index.html       # Página inicial
│   ├── registrar.html    # Página de registro
│   ├── login.html        # Página de login
│   ├── tarefas.html      # Página de visualização de tarefas
│   ├── adicionar_tarefa.html # Página para adicionar novas tarefas
│   └── atualizar_tarefa.html # Página para editar tarefas
└── static/              # Arquivos estáticos (CSS, JavaScript, imagens)
```