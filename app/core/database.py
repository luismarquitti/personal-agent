import os
import psycopg2
from dotenv import load_dotenv

# Carregar variáveis de ambiente do .env
load_dotenv()

def get_db_connection():
    """Retorna uma conexão com o banco de dados PostgreSQL."""
    try:
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST', 'localhost'),
            port=os.getenv('DB_PORT', '5432'),
            dbname=os.getenv('DB_NAME', 'personal_ai_core'),
            user=os.getenv('DB_USER', 'postgres'),
            password=os.getenv('DB_PASSWORD', 'yourpassword')
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        raise e

if __name__ == '__main__':
    # Teste rápido de conexão (opcional, só se tiver o DB rodando localmente)
    try:
        connection = get_db_connection()
        print("Conexão estabelecida com sucesso!")
        connection.close()
    except Exception:
        print("Falha na conexão local (esperado se não houver DB configurado).")
