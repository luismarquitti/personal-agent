# Breakdown Técnico: EP-03 Smart Home

## Fase 1: Setup/Fundação
- [ ] Tarefa 1.1: Configuração do ambiente e dependências do Canvas (instalar e configurar `react-konva` ou `d3.js`).
- [ ] Tarefa 1.2: Desenvolver biblioteca de ativos (SVG) para ícones Zigbee/Matter e registrar no código.
- [ ] Tarefa 1.3: Desenhar API de upload estruturada no backend/Cloud Functions.

## Fase 2: Implementação Core
- [ ] Tarefa 2.1: Implementar componente base de Canvas com Zoom, Pan e suporte Drag-and-Drop (Frontend).
- [ ] Tarefa 2.2: Criar lógica e interface de upload de imagens para o dashboard.
- [ ] Tarefa 2.3: Implementar node no LangGraph para análise de imagem via Gemini 2.5 Pro.
- [ ] Tarefa 2.4: Criar prompt de sistema para identificação de zonas de interesse na planta e retorno estruturado.

## Fase 3: Integração/UI
- [ ] Tarefa 3.1: Implementar API de posicionamento sugestivo de dispositivos e integrar a resposta (X, Y, Tipo) com o Canvas Frontend.
- [ ] Tarefa 3.2: Criar fluxo de edição (Human-in-the-loop) para o usuário mover os ícones sugeridos renderizados na UI.
- [ ] Tarefa 3.3: Implementar gerador de código YAML para Home Assistant a partir dos itens em tela e recurso de exportação.

## Fase 4: Testes e Polimento
- [ ] Tarefa 4.1: Escrever testes unitários para a geração de lógica YAML.
- [ ] Tarefa 4.2: Testar usabilidade do Canvas em diferentes tamanhos de tela.
- [ ] Tarefa 4.3: Validar a resiliência do node multimodal e resposta do LangGraph.

## QA & Segurança Check (Obrigatório)
- [ ] **RBAC:** Quais Custom Claims são necessárias para o upload e manipulação do projeto IoT? *(O usuário deve estar autenticado)*
- [ ] **Firestore:** Novas coleções (ex: Projetos Smart Home) exigem atualização de `firestore.rules`? (Sim, usuários só podem acessar os seus próprios projetos)
- [ ] **LGPD:** A feature manipula dados sensíveis de pacientes? (Neste caso, projetos residenciais sensíveis; deve possuir Storage restrito)
- [ ] **Testes Críticos:** Identificar os paths que precisam de cobertura de teste: autorização de upload/download de projeto.
- [ ] **Cloud Functions:** As chamadas para Gemini API devem estar protegidas em Functions, não executadas via cliente.

## Verificação Final
- [ ] Upload de planta baixa funciona sem travamentos.
- [ ] A IA posiciona sensores em cômodos lógicos (ex: PIR em cantos, Termostato em zonas centrais).
- [ ] Exportação gera YAML válido.
- [ ] Todos os critérios de aceite atendidos.
- [ ] Sem erros no console.
- [ ] firestore.rules atualizado.
- [ ] DoD atendido conforme PRD.md.
