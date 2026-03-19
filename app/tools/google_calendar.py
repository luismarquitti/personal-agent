import os
import datetime
from langchain_core.tools import tool
from googleapiclient.discovery import build
from app.core.google_auth import get_google_credentials

# Fixando para o default_user neste MVP
USER_ID = "default_user"

@tool
def get_todays_calendar_events() -> str:
    """Busca os compromissos do usuário no Google Calendar previstos para o dia de hoje."""
    try:
        creds = get_google_credentials(USER_ID)
        service = build('calendar', 'v3', credentials=creds)

        # Determina o início e fim do dia atual (em UTC por simplicidade ou fuso local)
        # Assumindo execução no fuso local:
        now = datetime.datetime.now()
        start_of_day = now.replace(hour=0, minute=0, second=0, microsecond=0).isoformat() + 'Z'
        end_of_day = now.replace(hour=23, minute=59, second=59, microsecond=999999).isoformat() + 'Z'

        events_result = service.events().list(
            calendarId='primary',
            timeMin=start_of_day,
            timeMax=end_of_day,
            singleEvents=True,
            orderBy='startTime'
        ).execute()
        
        events = events_result.get('items', [])

        if not events:
            return "Nenhum compromisso marcado para hoje."

        output = ["Compromissos para hoje:"]
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            # formata p/ facilitar leitura "14:00 - Reunião"
            time_str = start.split('T')[1][:5] if 'T' in start else 'Dia inteiro'
            output.append(f"- {time_str}: {event['summary']}")
            
        return "\n".join(output)
    except Exception as e:
        return f"Erro ao buscar o calendário: {str(e)}"

from typing import Optional

@tool
def create_calendar_event(summary: str, is_all_day: bool, start_time: Optional[str] = None, end_time: Optional[str] = None) -> str:
    """Cria um novo evento no Google Calendar principal do usuário.
    
    Args:
        summary (str): Título do compromisso.
        is_all_day (bool): True se for um evento de dia inteiro.
        start_time (str, opcional): Data de início em ISO-8601 ex: '2026-03-18T14:00:00'. Ignorado se is_all_day for True (usa a data atual).
        end_time (str, opcional): Data de fim em ISO-8601 ex: '2026-03-18T15:00:00'. Ignorado se is_all_day for True.
    """
    try:
        creds = get_google_credentials(USER_ID)
        service = build('calendar', 'v3', credentials=creds)

        if is_all_day:
            today_str = datetime.datetime.now().strftime('%Y-%m-%d')
            event_body = {
                'summary': summary,
                'start': {'date': today_str},
                'end': {'date': today_str}
            }
        else:
            if not start_time or not end_time:
                return "Erro: Para eventos que não são de dia inteiro, start_time e end_time são obrigatórios."
            event_body = {
                'summary': summary,
                'start': {'dateTime': start_time, 'timeZone': 'UTC'},
                'end': {'dateTime': end_time, 'timeZone': 'UTC'}
            }

        event = service.events().insert(calendarId='primary', body=event_body).execute()
        return f"Evento '{summary}' criado com sucesso (Link: {event.get('htmlLink')})."
    except Exception as e:
        return f"Erro ao criar o compromisso no calendário: {str(e)}"
