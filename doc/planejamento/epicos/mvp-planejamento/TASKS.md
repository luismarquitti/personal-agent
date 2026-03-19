# Breakdown Técnico: MVP Planejamento Diário com IA (EP-07)

## Fase 1: Setup/Fundação
- [ ] Tarefa 1.1: Configurar projeto no Google Cloud Console e habilitar APIs (Google Calendar API e Google Tasks API).
- [ ] Tarefa 1.2: Implementar fluxo de autenticação OAuth2 no backend (`app/`) para capturar e armazenar tokens (Access Token e Refresh Token) com segurança no PostgreSQL.

## Fase 2: Implementação Core (Backend / Agente)
- [ ] Tarefa 2.1: Desenvolver a Tool (LangGraph) para buscar compromissos do dia via Google Calendar API.
- [ ] Tarefa 2.2: Desenvolver a Tool (LangGraph) para buscar, criar e atualizar tarefas via Google Tasks API.
- [ ] Tarefa 2.3: Desenvolver a Tool (LangGraph) para agendar novos eventos no Google Calendar.
- [ ] Tarefa 2.4: Atualizar o prompt de sistema do Meta-Agente / Assistente Pessoal para utilizar essas ferramentas, analisar os dados retornados e gerar insights proativos (janelas de tempo, sobrecarga).

## Fase 3: Integração/UI (Frontend)
- [ ] Tarefa 3.1: Criar o componente `PlanningBoard` no React (`web/src/components/`) para renderizar os eventos, tarefas e insights de IA de forma visual (linha do tempo ou cards).
- [ ] Tarefa 3.2: Integrar o componente de Planejamento na interface principal (Command Center).
- [ ] Tarefa 3.3: Estabelecer comunicação em tempo real (WebSocket/SSE) para que a interface de planejamento atualize assim que o LLM terminar a execução e gerar os insights.

## Fase 4: Testes e Polimento
- [ ] Tarefa 4.1: Escrever testes unitários para as funções utilitárias que consomem as APIs do Google e para as Tools do agente.
- [ ] Tarefa 4.2: Testar ponta-a-ponta o fluxo OAuth (redirecionamento, armazenamento e expiração de token).
- [ ] Tarefa 4.3: Garantir responsividade da UI do painel de planejamento.

## Verificação Final
- [ ] Todos os critérios de aceite atendidos
- [ ] Sem erros no console
- [ ] Criptografia de tokens em repouso verificada
- [ ] DoD atendido (conforme Product_Roadmap.md)

---

## Checklist QA & Segurança

- [ ] **RBAC/Auth:** O sistema deve assegurar que cada usuário acesse exclusivamente as contas Google autorizadas com seu respectivo Access Token.
- [ ] **Data Stores:** Tokens OAuth *devem* ser criptografados em repouso no banco de dados (PostgreSQL).
- [ ] **LGPD e Privacidade:** Títulos e descrições de eventos e tarefas representam dados sensíveis (PII). Os logs do sistema não devem armazenar o conteúdo em texto claro das respostas da API do Google, mascarando informações nos logs de telemetria.
- [ ] **Testes Críticos:** Testar o cenário onde o refresh token é inválido ou revogado pelo usuário no painel do Google, exigindo reautenticação sem quebrar o chat do agente.
- [ ] **Cloud Functions/Backend:** A comunicação com o Google será feita estritamente via backend autenticado, nunca expondo tokens sensíveis para o frontend (React).
