---
name: tech-stack
description: "Define a arquitetura e as tecnologias mandatórias do projeto para evitar alucinações de bibliotecas."
---

# Tech Stack Rules

Sempre que atuar no Personal AI Core, o agente DEVE respeitar a stack tecnológica definida para garantir compatibilidade e manutenibilidade.

## Core Technologies
- **Backend:** Python 3.12+ (FastAPI).
- **Frontend:** React 19+ (Vite, TypeScript, Tailwind).
- **Banco de Dados:** PostgreSQL com extensão `pgvector` (via Docker).
- **IA Local:** Ollama (Llama 3, Phi-3).
- **Orquestração de IA:** LangChain / LangGraph.

## Regras de Escolha de Bibliotecas
1. **Preferência por Nativos:** Sempre prefira bibliotecas padrão do Python ou módulos integrados do React.
2. **Padrão de Dados:** Utilize `Pydantic v2` para esquemas de dados no backend e `Zod` no frontend.
3. **ORM/Query Builder:** Utilize o padrão já estabelecido no projeto (Drizzle ou Prisma). **NUNCA** introduza um novo ORM sem consulta prévia.
4. **Estado no Frontend:** Utilize `Zustand` para estado global simples.

## O Que Não Fazer (Don'ts)
- Não utilize bibliotecas de IA que não sejam LangChain/LangGraph a menos que a Spec peça explicitamente.
- Não introduza componentes UI fora do `Tailwind CSS`.
- Não sugira o uso de bancos NoSQL (MongoDB, etc) para dados relacionais.
