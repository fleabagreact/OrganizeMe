from datetime import date
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="sistema_tarefas"
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
    def adicionar_tarefa(usuario_id, titulo, descricao, data_limite, id_status, id_prioridade, id_categoria):
        data_criacao = date.today()
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
    def listar_tarefas(usuario_id, categoria_id=None, prioridade_id=None, status_id=None, data_inicio=None, data_fim=None):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        # Base query
        query = '''
            SELECT t.*, st.descricao as status, pt.descricao as prioridade, ct.descricao as categoria
            FROM tarefas t
            JOIN status_tarefa st ON t.id_status = st.id_status
            JOIN prioridade_tarefa pt ON t.id_prioridade = pt.id_prioridade
            JOIN categoria_tarefa ct ON t.id_categoria = ct.id_categoria
            WHERE t.usuario_id = %s
        '''
        params = [usuario_id]

        # Apply filters dynamically
        if categoria_id is not None:
            query += ' AND t.id_categoria = %s'
            params.append(categoria_id)

        if prioridade_id is not None:
            query += ' AND t.id_prioridade = %s'
            params.append(prioridade_id)

        if status_id is not None:
            query += ' AND t.id_status = %s'
            params.append(status_id)

        if data_inicio is not None:
            query += ' AND t.data_limite >= %s'
            params.append(data_inicio)

        if data_fim is not None:
            query += ' AND t.data_limite <= %s'
            params.append(data_fim)

        cursor.execute(query, params)
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
    def atualizar_tarefa(tarefa_id, titulo, descricao, data_limite, id_status, id_prioridade, id_categoria):
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(''' 
            UPDATE tarefas 
            SET titulo = %s, descricao = %s, data_limite = %s, id_status = %s, 
                id_prioridade = %s, id_categoria = %s 
            WHERE id_tarefa = %s
        ''', (titulo, descricao, data_limite, id_status, id_prioridade, id_categoria, tarefa_id))
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def buscar_tarefa_por_id(tarefa_id):
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute('SELECT * FROM tarefas WHERE id_tarefa = %s', (tarefa_id,))
        tarefa = cursor.fetchone()
        cursor.close()
        connection.close()
        return tarefa
