import os
import yaml
from typing import List, Optional, Dict, Any
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from app.core.database import get_db_connection

# Configuração de Embeddings (Usa Google Gemini por padrão conforme tech-stack)
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

def update_knowledge_base(file_path: str, metadata: Optional[Dict[str, Any]] = None):
    """
    Carrega um PDF, divide em chunks, gera embeddings e salva no banco.
    Atende Task 2.1 e 2.2.
    """
    if not os.path.exists(file_path):
        return {"error": f"Arquivo não encontrado: {file_path}"}

    try:
        # 1. Load
        loader = PyPDFLoader(file_path)
        docs = loader.load()

        # 2. Split
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )
        chunks = text_splitter.split_documents(docs)

        # 3. Embed & Store
        conn = get_db_connection()
        cur = conn.cursor()

        for chunk in chunks:
            content = chunk.page_content
            # Gera embedding
            vector = embeddings.embed_query(content)
            
            # Merge metadata
            final_metadata = chunk.metadata.copy()
            if metadata:
                final_metadata.update(metadata)

            import json
            cur.execute(
                """
                INSERT INTO knowledge_base (content, embedding, metadata, source_uri)
                VALUES (%s, %s, %s, %s)
                """,
                (content, vector, json.dumps(final_metadata), file_path)
            )

        conn.commit()
        cur.close()
        conn.close()

        return {"status": "success", "chunks_processed": len(chunks)}
    except Exception as e:
        return {"error": str(e)}

def query_knowledge_base(query: str, top_k: int = 5):
    """
    Realiza busca semântica no Vector DB.
    Atende Task 2.3.
    """
    try:
        # 1. Gera embedding da query
        query_vector = embeddings.embed_query(query)

        # 2. Busca no Postgres usando pgvector (cosine similarity)
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute(
            """
            SELECT content, metadata, source_uri, 1 - (embedding <=> %s::vector) as similarity
            FROM knowledge_base
            ORDER BY embedding <=> %s::vector
            LIMIT %s
            """,
            (query_vector, query_vector, top_k)
        )

        results = []
        for row in cur.fetchall():
            results.append({
                "content": row[0],
                "metadata": row[1],
                "source": row[2],
                "score": float(row[3])
            })

        cur.close()
        conn.close()

        if not results:
            return [{
                "content": "Desculpe, não encontrei informações específicas sobre isso na minha base de conhecimento atual. Posso tentar uma busca geral se desejar.",
                "metadata": {"type": "fallback"},
                "source": None,
                "score": 0.0
            }]

        return results
    except Exception as e:
        return {"error": str(e)}

# Ferramentas de Hardware IoT (Task 1.2/3.1 Backend Support)
def add_iot_product(name: str, brand: str, protocol: str, payload_yaml: str, metadata: Optional[Dict] = None):
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        import json
        cur.execute(
            """
            INSERT INTO iot_products (name, brand, protocol, payload_yaml, metadata)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id
            """,
            (name, brand, protocol, payload_yaml, json.dumps(metadata or {}))
        )
        product_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return {"status": "success", "id": product_id}
    except Exception as e:
        return {"error": str(e)}
