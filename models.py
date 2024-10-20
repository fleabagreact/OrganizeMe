import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password=" ",
        database="gerenciador_tarefas"
    )

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

class Tarefa:
    @staticmethod
    def adicionar_tarefa(usuario_id, descricao, prioridade, data_limite):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('INSERT INTO tarefas (usuario_id, descricao, prioridade, data_limite) VALUES (%s, %s, %s, %s)', 
                       (usuario_id, descricao, prioridade, data_limite))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def listar_tarefas(usuario_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM tarefas WHERE usuario_id = %s', (usuario_id,))
        tarefas = cursor.fetchall()
        cursor.close()
        connection.close()
        return tarefas

    @staticmethod
    def excluir_tarefa(tarefa_id):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('DELETE FROM tarefas WHERE id = %s', (tarefa_id,))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def buscar_tarefa_por_id(tarefa_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM tarefas WHERE id = %s', (tarefa_id,))
        tarefa = cursor.fetchone()
        cursor.close()
        connection.close()
        return tarefa

    @staticmethod
    def atualizar_tarefa(tarefa_id, descricao, prioridade, data_limite):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('UPDATE tarefas SET descricao = %s, prioridade = %s, data_limite = %s WHERE id = %s', 
                       (descricao, prioridade, data_limite, tarefa_id))
        connection.commit()
        cursor.close()
        connection.close()
