from langchain_core.tools import tool
from typing import List, Dict, Any

@tool
def update_planning_dashboard(
    daily_items: List[Dict[str, str]], 
    weekly_items: List[Dict[str, str]], 
    monthly_items: List[Dict[str, str]]
) -> str:
    """Atualiza a visão do Dashboard de Planejamento do usuário (3 camadas).
    Deve ser chamada SOMENTE após o usuário confirmar explicitamente que deseja a atualização visual no painel.
    
    Args:
        daily_items (List[Dict[str, str]]): Tarefas e eventos diários. Requer as chaves 'id', 'title', e 'status' ('pending', 'in_progress', 'completed').
        weekly_items (List[Dict[str, str]]): Metas semanais. Requer chaves 'id', 'title', 'status'.
        monthly_items (List[Dict[str, str]]): Objetivos mensais. Requer chaves 'id', 'title', 'status'.
        
    Returns:
        str: Feedback de sucesso da sincronização.
    """
    
    payload = {
        "type": "DASHBOARD_UPDATE",
        "data": {
            "daily": daily_items,
            "weekly": weekly_items,
            "monthly": monthly_items
        }
    }
    
    # TODO: Fase 3 - Emitir evento WebSocket para os clientes conectados
    print(f"WS Payload Prepared: {payload}")
    
    return "Dashboard atualizado com sucesso."
