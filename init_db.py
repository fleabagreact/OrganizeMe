import mysql.connector

db_config = {
    'user': 'root',
    'password': 'aluno',
    'host': 'localhost',
}

def create_database():
    conn = None
    try:
        conn = mysql.connector.connect(
            host=db_config['host'],
            user=db_config['user'],
            password=db_config['password']
        )
        cursor = conn.cursor()

        print("Conexão estabelecida com sucesso ao servidor MySQL.")

        with open('database/schema.sql', 'r') as file:
            schema_sql = file.read()

        for statement in schema_sql.split(';'):
            if statement.strip():
                print(f"Executando SQL: {statement.strip()}")
                cursor.execute(statement)

        print("Banco de dados e tabelas configurados com sucesso.")

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