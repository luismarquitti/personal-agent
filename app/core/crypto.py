import os
from cryptography.fernet import Fernet
from dotenv import load_dotenv

load_dotenv()

# Pegar uma chave de encriptação do .env
ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")
if not ENCRYPTION_KEY:
    raise ValueError("A variável de ambiente ENCRYPTION_KEY não está configurada.")

# Fernet exige que a chave seja em bytes
fernet = Fernet(ENCRYPTION_KEY.encode())

def encrypt_data(data: str) -> str:
    """Encripta uma string."""
    return fernet.encrypt(data.encode()).decode()

def decrypt_data(token: str) -> str:
    """Decripta uma string encriptada."""
    return fernet.decrypt(token.encode()).decode()
