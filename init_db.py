import mysql.connector

db_config = {
    'user': 'root',
    'password': '',  # Sem senha, assumindo o uso de XAMPP
    'host': 'localhost',
}

def create_database():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS gerenciador_tarefas")
        print("Banco de dados 'gerenciador_tarefas' criado ou já existente.")

        cursor.close()
        conn.close()

        db_config['database'] = 'gerenciador_tarefas'
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        print("Conexão estabelecida com sucesso ao banco de dados 'gerenciador_tarefas'.")

        with open('database/schema.sql', 'r') as file:
            schema_sql = file.read()

        for statement in schema_sql.split(';'):
            if statement.strip():
                cursor.execute(statement)

        print("Tabelas criadas com sucesso.")

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
