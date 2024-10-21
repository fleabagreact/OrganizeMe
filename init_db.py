import mysql.connector

db_config = {
    'user': 'root',
    'password': 'aluno',
    'host': 'localhost',
}

def create_database():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS sistema_tarefas")
        print("Banco de dados 'sistema_tarefas' criado ou já existente.")

        db_config['database'] = 'sistema_tarefas'
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        print("Conexão estabelecida com sucesso ao banco de dados 'sistema_tarefas'.")

        with open('database/schema.sql', 'r') as file:
            schema_sql = file.read()

        for statement in schema_sql.split(';'):
            if statement.strip():
                cursor.execute(statement)

        print("Tabelas criadas com sucesso.")

        cursor.execute("SELECT COUNT(*) FROM status_tarefa")
        status_count = cursor.fetchone()[0]
        if status_count == 0:
            cursor.execute("INSERT INTO status_tarefa (descricao) VALUES ('Concluída'), ('Em andamento'), ('Pendente')")
            cursor.execute("INSERT INTO prioridade_tarefa (descricao) VALUES ('Baixa'), ('Média'), ('Alta')")
            cursor.execute("INSERT INTO categoria_tarefa (descricao) VALUES ('Trabalho'), ('Estudo'), ('Pessoal')")
            print("Dados iniciais inseridos com sucesso.")

    except mysql.connector.Error as erro:
        print(f"Erro ao conectar ou criar banco de dados: {erro}")

    finally:
        if conn is not None and conn.is_connected():
            conn.commit()
            cursor.close()
            conn.close()
            print("Conexão encerrada.")

if __name__ == '__main__':
    create_database()
