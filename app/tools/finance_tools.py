import os
import pandas as pd
from typing import List, Dict, Any, Optional
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from app.core.llm_factory import get_llm
from app.models.finance import TransactionCreate, TransactionType

@tool
def extract_financial_data(file_path: str) -> str:
    """
    Extrai dados financeiros de arquivos (PDF, CSV, XLSX, Imagens).
    Retorna uma lista de transações encontradas em formato amigável.
    """
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext in ['.csv', '.xlsx', '.xls']:
        return _extract_from_spreadsheet(file_path, ext)
    elif ext in ['.pdf', '.jpg', '.jpeg', '.png']:
        return _extract_with_vision(file_path)
    else:
        return f"Formato de arquivo {ext} não suportado para extração financeira."

def _extract_from_spreadsheet(file_path: str, ext: str) -> str:
    try:
        if ext == '.csv':
            df = pd.read_csv(file_path)
        else:
            df = pd.read_excel(file_path)
        
        # Converte para string para o LLM processar ou retorna resumo
        # Para o MVP, vamos apenas retornar o conteúdo das primeiras linhas
        data_str = df.head(10).to_string()
        return f"Dados brutos da planilha:\n{data_str}\n\nPor favor, peça ao usuário para confirmar quais desses itens devem ser importados."
    except Exception as e:
        return f"Erro ao ler planilha: {str(e)}"

def _extract_with_vision(file_path: str) -> str:
    try:
        llm = get_llm()
        if not hasattr(llm, "model") or "gemini" not in llm.model.lower():
             # Fallback ou aviso se não for Gemini (que suporta visão nativamente no factory)
             # Nota: O factory get_llm() retorna ChatGoogleGenerativeAI se for google.
             pass

        prompt = """Analise este documento financeiro (recibo, nota fiscal, extrato ou boleto).
        Extraia as seguintes informações em formato JSON:
        - data (formato ISO YYYY-MM-DD)
        - valor (float)
        - descricao (string)
        - categoria_sugerida (string)
        - tipo (income ou expense)

        Retorne APENAS o JSON ou uma lista de JSONs se houver múltiplas transações.
        """
        
        # Para imagens/PDFs no LangChain Google GenAI, enviamos como conteúdo multimídia
        # Nota: LangChain requer bytes ou URL. Aqui simulamos o envio do caminho para processamento futuro.
        # No ambiente real, precisaríamos ler os bytes:
        with open(file_path, "rb") as f:
            image_data = f.read()

        import base64
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        
        # Formato esperado pelo LangChain Google GenAI para multimídia
        message = HumanMessage(
            content=[
                {"type": "text", "text": prompt},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                },
            ]
        )
        
        response = llm.invoke([message])
        return f"Extração concluída:\n{response.content}"
    except Exception as e:
        return f"Erro na extração via visão: {str(e)}"

@tool
def generate_financial_summary(user_id: int = 1) -> str:
    """
    Gera um resumo textual das finanças do usuário para o chat.
    Inclui saldos de contas e transações recentes.
    """
    from app.crud import finance as crud
    try:
        accounts = crud.get_accounts(user_id)
        transactions = crud.get_transactions(user_id)
        
        summary = "### Resumo Financeiro Atual\n\n"
        summary += "**Saldos por Conta:**\n"
        for acc in accounts:
            summary += f"- {acc['name']}: R$ {acc['balance']:.2f}\n"
        
        summary += "\n**Transações Recentes:**\n"
        for t in transactions[:5]:
            summary += f"- {t['date'].strftime('%d/%m')}: {t['description']} (R$ {t['amount']:.2f})\n"
            
        return summary
    except Exception as e:
        return f"Erro ao gerar resumo: {str(e)}"
