import os
import logging
from typing import Optional

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

logger = logging.getLogger(__name__)


def get_llm() -> BaseChatModel:
    """
    Factory function que retorna um BaseChatModel conforme LLM_PROVIDER.

    Variáveis de ambiente:
        LLM_PROVIDER (str): "google" | "ollama" — padrão: "google"
        GOOGLE_MODEL (str): nome do modelo Gemini — padrão: "gemini-2.5-flash"
        OLLAMA_MODEL (str): nome do modelo Ollama — padrão: "llama3"
        OLLAMA_BASE_URL (str): URL do servidor Ollama — padrão: "http://localhost:11434"

    Raises:
        ValueError: se LLM_PROVIDER contiver um valor não suportado.
    """
    provider = os.getenv("LLM_PROVIDER", "google").lower().strip()

    if provider == "google":
        model = os.getenv("GOOGLE_MODEL", "gemini-2.5-flash")
        logger.info(f"[LLM] Provider: google | Model: {model}")
        return ChatGoogleGenerativeAI(model=model, temperature=0.2)

    elif provider == "ollama":
        model = os.getenv("OLLAMA_MODEL", "llama3")
        base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

        # Verificação de disponibilidade (não-bloqueante)
        _check_ollama_health(base_url)

        logger.info(f"[LLM] Provider: ollama | Model: {model} | URL: {base_url}")
        return ChatOllama(model=model, base_url=base_url)

    else:
        raise ValueError(
            f"[LLM] Provider desconhecido: '{provider}'. "
            f"Valores suportados: 'google', 'ollama'. "
            f"Verifique a variável de ambiente LLM_PROVIDER no seu .env."
        )


def _check_ollama_health(base_url: str) -> None:
    """
    Verifica se o servidor Ollama está acessível.
    Apenas loga um warning — não levanta exceção.
    """
    try:
        import urllib.request

        url = f"{base_url.rstrip('/')}/api/tags"
        req = urllib.request.Request(url, method="GET")
        with urllib.request.urlopen(req, timeout=3) as response:
            if response.status == 200:
                logger.info(f"[LLM] Ollama disponível em {base_url}")
    except Exception as e:
        logger.warning(
            f"[LLM] Ollama não está disponível em {base_url}. "
            f"Certifique-se de que o servidor Ollama está rodando. Erro: {e}"
        )
