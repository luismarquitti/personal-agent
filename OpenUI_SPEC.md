Com base na estrutura e nos arquivos do projeto **`personal-agent`** que você compartilhou (como a presença do Vite, FastAPI, LangGraph, WebSockets e as pastas `web/src/components/dynamic`), adaptei o rascunho da sua especificação para refletir perfeitamente a arquitetura real do seu repositório. 

Aqui está a especificação refinada pronta para ser usada como guia de implementação ou PRD (Product Requirements Document) no seu projeto:

***

# SPEC: Interface Gerativa para o Personal Agent

## 1. Visão Geral do Projeto
O objetivo é evoluir a interface do `personal-agent` para uma **Agent-Driven Interface (Interface Gerativa)** moderna e responsiva. O assistente, impulsionado por LangGraph, gerencia rotinas, finanças, infraestrutura e planejamento. Utilizaremos o **OpenUI** para transitar de um chat baseado estritamente em texto para uma interface onde o agente pode renderizar, atualizar e manipular componentes visuais nativos do React em tempo real, com alta eficiência e baixo consumo de tokens.

## 2. Arquitetura e Stack Tecnológico (Alinhado ao Repositório)
* **Backend (Lógica e Estado):** Python, FastAPI, LangGraph (`app/core/graph.py`), LangChain.
* **Frontend (Interface):** React com Vite (`web/vite.config.ts`), Tailwind CSS, Radix UI / Shadcn UI (para componentes base).
* **Gerenciamento de Estado:** Zustand (`useChatStore.ts`, `usePlanningStore.ts`, `useSystemStore.ts`).
* **Motor de Renderização UI:** OpenUI (integrado ao `DynamicRegistry.tsx` e `DynamicRenderer.tsx` existentes).
* **Comunicação (Transporte):** WebSockets nativos já presentes no projeto (`web/src/lib/useSocket.ts` e `app/api/middleware.py` / testes em `test_websocket.py`) para streaming em tempo real.

## 3. Topologia da Interface (Layout UI/UX)
A interface adotará o padrão de **Tela Dividida (Split-Screen)**, aproveitando os componentes modulares já desenhados na pasta `components/dashboard`:
* **Painel de Estado (Esquerda / Principal):** Visão geral dinâmica e atualizável. Contém os dashboards persistentes:
    * *Planning Dashboard* (`PlanningDashboard.tsx`): Timeline, agenda e tarefas Kanban.
    * *Finance Dashboard* (`FinanceDashboard.tsx`): Resumo financeiro e insights.
    * *System/Hardware Dashboard* (`SystemDashboard.tsx`, `HardwareCatalog.tsx`): Status da infraestrutura.
* **Painel Interativo (Direita / Lateral):** A interface de Chat do Agente.
    * Input de texto/comandos.
    * Histórico da conversa (`ChatMessage.tsx`) onde o **OpenUI** renderizará componentes dinâmicos *inline* (ex: um formulário de adição de despesa ou um card interativo de confirmação de reunião).

## 4. O Papel do OpenUI (Motor Gerativo)
O OpenUI atuará como a ponte de tradução entre o raciocínio do LangGraph e a árvore de componentes do React, evitando que o LLM precise cuspir JSONs complexos e propensos a erro.
* **Registro de Componentes (Frontend):** Os componentes de UI do projeto serão injetados no OpenUI através do `web/src/components/dynamic/DynamicRegistry.tsx`.
* **Injeção de Contexto (Backend):** O backend instruirá o OpenUI a gerar esquemas descritivos dos componentes React e injetá-los no prompt de sistema do agente no `app/core/llm_factory.py` ou `graph.py`.
* **Streaming Eficiente:** Quando o agente invocar uma visualização, utilizará a marcação do `openui-lang`. O frontend parseará esse stream dinamicamente pelo `DynamicRenderer.tsx`, mostrando a UI renderizada palavra por palavra.

## 5. Fluxo de Interação (Data Flow)
**Cenário de Exemplo:** O usuário digita: *"Lance uma despesa de R$ 50 no Uber e remarque minha daily para amanhã."*
1.  **Input:** Frontend envia a mensagem de texto pelo WebSocket (`useSocket.ts`).
2.  **Processamento:** O `graph.py` processa a intenção, utilizando as tools de finanças (`app/tools/finance_tools.py`) e de agenda (`app/tools/google_calendar.py`).
3.  **Geração OpenUI:** O LangGraph formula a resposta e emite o bloco OpenUI correspondente a `<CardDespesa status="sucesso" valor="50" />` e `<CardReuniao atualizada={true} />`.
4.  **Renderização (Chat):** O `DynamicRenderer.tsx` intercepta a marcação OpenUI do WebSocket e renderiza os dois componentes React iterativamente no histórico do chat.
5.  **Sincronização Global:** As mutações disparam atualizações no Zustand (`usePlanningStore` e `useSystemStore`), forçando os Dashboards do Painel Esquerdo a refletirem o novo estado silenciosamente.

## 6. Roadmap de Implementação (Fases)

### Fase 1: Preparação do Backend (FastAPI + LangGraph)
* **Streaming via WS:** Garantir que o agente no `app/core/graph.py` consiga emitir (yield) as respostas parciais (tokens) em tempo real pelos WebSockets gerenciados no FastAPI.
* **Registro de Ferramentas UI:** Integrar a definição de output do OpenUI nas ferramentas/LLM (`llm_factory.py`), garantindo que o LLM compreenda o catálogo de UI disponível.
* **Sincronização de Estado:** Assegurar que as chamadas às APIs CRUD (ex: `app/crud/finance.py`) emitam eventos de invalidação para que o frontend saiba quando fazer *refetch* dos dashboards.

### Fase 2: Adaptação do Frontend (Vite + React + OpenUI)
* **Instalação:** Adicionar as dependências do OpenUI no `web/package.json`.
* **Dynamic Registry:** Atualizar o `web/src/components/dynamic/DynamicRegistry.tsx` para expor os componentes do Shadcn e componentes customizados (ex: `FinanceCard`, `TaskItem`) ao SDK do OpenUI.
* **Dynamic Renderer:** Refatorar o `web/src/components/dynamic/DynamicRenderer.tsx` para interceptar a sintaxe do OpenUI em vez de simples Markdown/JSON, suportando o streaming em tempo real.

### Fase 3: Integração Agente-Interface
* **Conexão de Stream:** Ajustar o `useChatStore.ts` e o `ChatMessage.tsx` para acoplar os chunks recebidos pelo WebSocket diretamente na engine do OpenUI.
* **Testes de Componentes:** Validar se o agente consegue renderizar nativamente gráficos, botões de ação e modais dentro da janela de chat.

### Fase 4: Polimento e UX
* **Fallbacks:** Implementar Error Boundaries no React. Se o LLM alucinar a sintaxe de um componente UI, o OpenUI ou o renderer deve cair graciosamente para uma resposta de texto padrão.
* **Ações Reversas:** Permitir que botões renderizados pelo OpenUI (ex: "Confirmar Cancelamento") enviem eventos de volta pelo WebSocket para o LangGraph continuar o fluxo (Human-in-the-loop).

***

**Próximos Passos Sugeridos:**
Você pode começar essa implementação criando uma branch `feat/openui-integration`. Recomendo iniciar refatorando o `DynamicRegistry.tsx` e o `DynamicRenderer.tsx` no frontend para suportar a ingestão dos componentes via OpenUI antes de alterar os prompts no backend.