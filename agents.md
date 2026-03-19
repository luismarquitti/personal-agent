# Personal AI Core - Jules Hints

Este repositório contém o **Personal AI Core**, um ecossistema modular de IA.

## Tecnologias Principais
- **Backend:** Python 3.12+ (FastAPI, LangGraph)
- **Frontend:** React 19+ (Vite, TypeScript, Tailwind)
- **Banco de Dados:** PostgreSQL (Docker)
- **IA Local:** Ollama

## Configuração do Ambiente
O script de inicialização recomendado para o Jules está em `.jules/setup.sh`.
Você pode executá-lo no painel de configuração do Jules.

## Comandos Úteis
- **Instalar tudo:** `npm run setup` (Nota: Use `.jules/setup.sh` no primeiro boot do Jules)
- **Backend Dev:** `uvicorn app.main:app --reload`
- **Frontend Dev:** `cd web && npm run dev`
- **Diagnóstico:** `python scripts/doctor.py`

## Estrutura de Agentes (.agents/)
As regras e skills deste repositório estão em `.agents/`. 
- **Skills:** Instruções específicas por domínio.
- **Workflows:** Procedimentos operacionais padrão (SOPs).
- **Rules:** Governança global (Commits atômicos, etc).
