import os
from langchain_core.tools import tool
from googleapiclient.discovery import build
from app.core.google_auth import get_google_credentials

# Fixando para o default_user neste MVP
USER_ID = "default_user"

@tool
def get_pending_tasks() -> str:
    """Busca as tarefas pendentes do usuário no Google Tasks (lista principal).
    Retorna uma lista resumida das tarefas.
    """
    try:
        creds = get_google_credentials(USER_ID)
        service = build('tasks', 'v1', credentials=creds)

        # Usando a tasklist padrão (@default) que representa "My Tasks"
        results = service.tasks().list(
            tasklist='@default',
            showCompleted=False,
            maxResults=20
        ).execute()
        
        items = results.get('items', [])

        if not items:
            return "Nenhuma tarefa pendente na lista principal."

        output = ["Tarefas Pendentes:"]
        for task in items:
            title = task.get('title', 'Sem título')
            status = task.get('status', '')
            output.append(f"- [ ] {title}")
            
        return "\n".join(output)
    except Exception as e:
        return f"Erro ao buscar tarefas: {str(e)}"

@tool
def create_google_task(title: str, notes: str = "") -> str:
    """Cria uma nova tarefa na lista principal (My Tasks) do Google Tasks.
    
    Args:
        title (str): O título/descrição curta da tarefa.
        notes (str, opcional): Notas ou descrição detalhada da tarefa.
    """
    try:
        creds = get_google_credentials(USER_ID)
        service = build('tasks', 'v1', credentials=creds)

        task_body = {
            'title': title,
            'notes': notes
        }

        result = service.tasks().insert(
            tasklist='@default',
            body=task_body
        ).execute()

        taskId = result.get('id')
        if taskId:
            return f"Tarefa '{title}' criada com sucesso!"
        else:
            return "A operação retornou, mas o ID da tarefa não pôde ser confirmado."
    except Exception as e:
        return f"Erro ao criar tarefa: {str(e)}"
