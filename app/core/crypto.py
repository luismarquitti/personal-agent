import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Pegar uma chave de encriptação do .env, ou usar uma default (não recomendado para produção)
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    # Se não houver chave no .env, vamos usar uma de fallback para desenvolvimento
    # 32 url-safe base64-encoded bytes
    ENCRYPTION_KEY = b'G-8gK4Qn4qC2K9J6G-8gK4Qn4qC2K9J6G-8gK4Qn4qA='
    
fernet = Fernet(ENCRYPTION_KEY)

def encrypt_data(data: str) -> str:
    """Encripta uma string."""
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    """Decripta uma string encriptada."""
    return fernet.decrypt(token.encode()).decode()
