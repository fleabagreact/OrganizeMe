from datetime import date
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

# Função para obter conexão com o banco de dados
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="aluno",
        database="sistema_tarefas"
    )

# Classe para gerenciar operações relacionadas ao usuário
class Usuario:    
    @staticmethod
    def criar_usuario(nome, email, senha):
        senha_hash = generate_password_hash(senha)
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO usuarios (nome, email, senha) VALUES (%s, %s, %s)', 
                       (nome, email, senha_hash))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def buscar_por_email(email):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE email = %s', (email,))
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        return usuario

    @staticmethod
    def buscar_por_id(usuario_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM usuarios WHERE id = %s', (usuario_id,))
        usuario = cursor.fetchone()
        cursor.close()
        connection.close()
        return usuario

    @staticmethod
    def verificar_senha(senha_hash, senha):
        return check_password_hash(senha_hash, senha)

# Classe para gerenciar operações relacionadas às tarefas
class Tarefa:
    @staticmethod
    def adicionar_tarefa(usuario_id, titulo, descricao, data_limite, id_status, id_prioridade, id_categoria):
        data_criacao = date.today()  # Define a data de criação como a data atual
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO tarefas 
            (usuario_id, titulo, descricao, data_criacao, data_limite, id_status, id_prioridade, id_categoria) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        ''', (usuario_id, titulo, descricao, data_criacao, data_limite, id_status, id_prioridade, id_categoria))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def listar_tarefas(usuario_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('''
            SELECT t.*, st.descricao as status, pt.descricao as prioridade, ct.descricao as categoria
            FROM tarefas t
            JOIN status_tarefa st ON t.id_status = st.id_status
            JOIN prioridade_tarefa pt ON t.id_prioridade = pt.id_prioridade
            JOIN categoria_tarefa ct ON t.id_categoria = ct.id_categoria
            WHERE t.usuario_id = %s
        ''', (usuario_id,))
        tarefas = cursor.fetchall()
        cursor.close()
        connection.close()
        return tarefas

    @staticmethod
    def excluir_tarefa(tarefa_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM tarefas WHERE id_tarefa = %s', (tarefa_id,))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def buscar_tarefa_por_id(tarefa_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('''
            SELECT t.*, st.descricao as status, pt.descricao as prioridade, ct.descricao as categoria
            FROM tarefas t
            JOIN status_tarefa st ON t.id_status = st.id_status
            JOIN prioridade_tarefa pt ON t.id_prioridade = pt.id_prioridade
            JOIN categoria_tarefa ct ON t.id_categoria = ct.id_categoria
            WHERE t.id_tarefa = %s
        ''', (tarefa_id,))
        tarefa = cursor.fetchone()
        cursor.close()
        connection.close()
        return tarefa

    @staticmethod
    def atualizar_tarefa(tarefa_id, titulo, descricao, data_limite, id_status, id_prioridade, id_categoria):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
            UPDATE tarefas 
            SET titulo = %s, descricao = %s, data_limite = %s, id_status = %s, id_prioridade = %s, id_categoria = %s
            WHERE id_tarefa = %s
        ''', (titulo, descricao, data_limite, id_status, id_prioridade, id_categoria, tarefa_id))
        connection.commit()
        cursor.close()
        connection.close()
