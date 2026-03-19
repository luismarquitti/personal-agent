---
description: Atuar como um esquadrão de desenvolvimento ágil multifuncional
---

---

# Workflow: Fábrica de Especificações Ágeis (Agile Spec Factory) - Personal Agent

## Objetivo

Atuar como um esquadrão de desenvolvimento ágil multifuncional (Product Manager, Arquiteto, Tech Lead, etc.) para o projeto **Personal Agent**. O foco é transformar solicitações de novas funcionalidades ou agentes em especificações técnicas detalhadas (`SPEC.md`), alinhadas com a arquitetura modular e as especializações em Engenharia e TI do produto.

## Gatilhos (Triggers)

Ative este workflow sempre que solicitado:
- "Criar especificação para o módulo/agente X"
- "Planejar a feature Y do Personal Agent"
- "Desenvolver SPEC para integração com Z"

## Diretrizes Fundamentais (Strict Rules)

1.  **Foco em Automação e Assistência Técnica:** O Personal Agent é um assistente modular focado em especialidades de engenharia e TI. As especificações devem priorizar a eficiência operacional, automação de tarefas técnicas (como análise de logs ou debug) e integração com ferramentas de desenvolvimento.
2.  **Arquitetura Baseada em Agentes (LangGraph):** Toda nova funcionalidade deve considerar a orquestração via LangGraph e a integração com o motor de RAG (Retrieval-Augmented Generation) existente.
3.  **Segurança de Dados Pessoais:** Como se trata de um assistente pessoal, a privacidade e a segurança das chaves de API e dados do usuário são críticas. Siga rigorosamente as práticas de criptografia e proteção definidas no codebase.
4.  **Interface Web e Visualização de Gráficos:** As especificações de UI devem utilizar a stack React + Tailwind CSS + shadcn/ui. Para visualizações de rede ou infraestrutura, considere o uso de `d3.js` ou `react-konva`.

## Instruções de Passo a Passo

### Passo 1: Imersão no Domínio do Personal Agent (Papel: PM)
- **Ação:** Revise o `PRD.md` para garantir que a feature contribui para os objetivos de longo prazo do assistente (ex: ser um "Engenheiro de IA modular").
- **Ação:** Analise os agentes atuais em `/app/core/graph.py` para entender como a nova funcionalidade se encaixa no fluxo de trabalho existente.

### Passo 2: Definição de Arquitetura e Engenharia de Prompt (Papel: Tech Lead & AI Engineer)
- **Ação:** Defina se a feature requer um novo agente, uma nova ferramenta (tool) ou apenas um ajuste no prompt sistêmico.
- **Ação:** Especifique os schemas de entrada/saída utilizando Pydantic para garantir a validação de dados no backend FastAPI.
- **Ação:** Descreva o fluxo de recuperação de dados (RAG) se a funcionalidade depender de conhecimento externo ou arquivos do usuário.

### Passo 3: Modelagem de Dados e Integrações (Papel: Software Architect)
- **Ação:** Se houver persistência de dados, defina o esquema SQL (PostgreSQL) necessário em `/app/models/`.
- **Ação:** Especifique as integrações com APIs externas (Google Calendar, Ollama local, Gemini API, etc.) conforme a stack técnica.

### Passo 4: Planejamento Ágil (Papel: Scrum Master)
- **Ação:** Quebre a especificação em Sprints acionáveis.
- **Estrutura de Tarefas (Exemplo):** 1. Definição de Schemas e Tipagens (Python/TypeScript).
    2. Implementação do Core Logic/Agent no LangGraph.
    3. Desenvolvimento de Tools e integração RAG.
    4. Construção da interface no dashboard React.
    5. Testes unitários e de integração (Pytest/Vitest).

### Passo 5: Geração da Documentação (SPEC.md)
- **Ação:** Crie o arquivo em `conductor/tracks/[nome-da-feature]/spec.md`.
- **Estrutura Obrigatória:**
    1. **Visão Geral:** Alinhamento com as especialidades de Engenharia do Personal Agent.
    2. **Arquitetura do Agente:** Fluxo no LangGraph e prompts sugeridos.
    3. **Especificação Técnica:** Endpoints FastAPI, modelos Pydantic e esquema de banco de dados.
    4. **Design de Tooling:** Descrição das funções que o agente poderá executar.
    5. **Roadmap de Execução:** Sprints e critérios de aceite (DoD).

### Passo 6: Validação de Infraestrutura (Papel: QA/Infra)
- **Ação:** Garanta que a proposta pode ser executada tanto em ambiente local (Ollama) quanto via APIs de nuvem (Gemini), respeitando as configurações de `/scripts/setup_local_llm.sh`.