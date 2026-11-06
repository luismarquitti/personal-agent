---
name: openclaw-cron-manager
description: >
  Cria, edita, lista e gerencia Cron Jobs nativos do OpenClaw (`openclaw cron`)
  e entradas HEARTBEAT.md. Use SEMPRE que o usuário mencionar: agendar tarefa,
  criar cron, editar heartbeat, automatizar no OpenClaw, configurar agendamento,
  rotina automática, job recorrente, openclaw schedule, "quero que o OpenClaw
  faça X toda hora/dia/semana", pipeline agendado, prompt recorrente, skill
  agendada, ou qualquer variante de automação periódica dentro do ecossistema
  OpenClaw. Dispare também quando o usuário perguntar "quais crons tenho?" ou
  "o que está agendado no meu OpenClaw?".
---

# OpenClaw Cron Manager

Orquestra o ciclo completo de criação e gestão de automações agendadas no
ecossistema OpenClaw: entende o objetivo, recomenda o mecanismo correto,
planeja o modelo e prompt mais eficiente em tokens, e gera os artefatos
prontos para instalação.

---

## Arquitetura da Skill

```
openclaw-cron-manager/
├── SKILL.md                        ← Este arquivo (fluxo principal)
└── references/
    ├── decision-guide.md           ← OpenClaw Cron vs Heartbeat vs Linux Cron
    ├── cron-templates.md           ← Templates CLI openclaw cron por categoria
    ├── heartbeat-templates.md      ← Templates de HEARTBEAT.md por categoria
    ├── prompt-optimizer.md         ← Seleção de modelo multi-provider + otimização
    └── telegram-templates.md       ← Biblioteca de templates de output Telegram
```

Leia o reference file relevante **conforme o passo** — não carregue todos de uma vez.

---

## Conceito Fundamental

O OpenClaw tem **seu próprio sistema de cron integrado ao Gateway** — completamente
diferente do `crontab` do Linux:

| OpenClaw Cron | Linux Cron |
|---------------|------------|
| `openclaw cron add` | `crontab -e` |
| Jobs persistem em SQLite | Arquivo crontab |
| Executa **prompts de LLM** diretamente | Executa comandos shell |
| Delivery nativo (Telegram, Slack, etc.) | Sem delivery integrado |
| Histórico de runs + retry automático | Sem histórico |
| Override de modelo por job | N/A |

Linux cron é usado apenas para tarefas **sem IA** (backups, limpeza de arquivos).
Para qualquer coisa com IA → `openclaw cron`.

---

## Fluxo Principal (5 Passos)

### Passo 1 — Entender o Objetivo (Elicitação Obrigatória)

Antes de qualquer geração, **sempre** colete as informações abaixo. Se o usuário
já forneceu algumas, pule as que forem claras e pergunte apenas o que falta.

**Perguntas-chave:**

1. **O que a automação deve fazer?**
   - Executar uma tarefa de sistema sem IA (backup, limpeza, rsync)
   - Monitorar algo e alertar por Telegram apenas se houver anomalia
   - Gerar um relatório/resumo periódico via IA
   - Sincronizar dados entre sistemas (Notion, GitHub, etc.)
   - Lembrete one-shot (ex: "em 30 minutos, verificar X")
   - Outro (descrever)

2. **Com que frequência?**
   - Intervalo fixo: a cada N minutos/horas (`--every`)
   - Horário específico diário/semanal (expressão cron `--cron`)
   - One-shot em horário/intervalo específico (`--at`)

3. **Precisa de processamento por IA (LLM)?**
   - Sim — formatar, resumir, analisar, decidir, responder
   - Não — executar script puro, backup, operação de arquivo

4. **O job precisa de contexto entre execuções?**
   - Não — cada run é independente (→ `--session isolated`)
   - Sim — acumula histórico (→ `--session session:custom-id`)
   - É ambient na sessão principal (→ HEARTBEAT.md)

5. **Qual a saída esperada?**
   - Mensagem Telegram (canal ou DM)
   - Outro canal (Slack, Discord)
   - Webhook HTTP externo
   - Sem entrega (log apenas)

Após coletar, vá ao **Passo 2**.

---

### Passo 2 — Recomendar o Mecanismo

Leia `references/decision-guide.md` e aplique a árvore de decisão.

Apresente ao usuário:
- **Mecanismo recomendado** (OpenClaw Cron, Heartbeat, ou Linux Cron)
- **Justificativa em 2-3 linhas**
- **Alternativa e trade-off** (quando relevante)

Aguarde confirmação antes de avançar.

---

### Passo 3 — Planejar Modelo e Prompt

**Somente se o job envolver processamento por IA.** Leia `references/prompt-optimizer.md`.

**Fluxo obrigatório:**
1. Execute (ou peça ao usuário) `openclaw models list` para identificar o que está disponível
2. Avalie modelos na ordem: **local (Ollama) → free cloud (OpenRouter :free) → paid cloud**
3. Selecione o modelo mais leve suficiente para a complexidade da tarefa

Apresente ao usuário:
```
✅ Recomendado: [modelo local ou free]  (custo: zero)
🔄 Fallback:    [próximo tier]
💰 Se precisar: [modelo pago]
Justificativa:  [por que esse tier é suficiente]
```

Defina também: estratégia de prompt, estimativa de tokens/run, se usa `--thinking high`.

---

### Passo 4 — Selecionar Template Telegram e Gerar os Artefatos

**4a — Selecionar template Telegram** (se o job envia ao Telegram):
Leia `references/telegram-templates.md` e identifique o template adequado:

| Situação | Template |
|----------|----------|
| Só envia se detectar problema | T-01 Alerta |
| Relatório sempre no horário | T-02 Relatório Periódico |
| Lista de itens (issues, PRs, tasks) | T-03 Resumo de Lista |
| Resumo de um período (dia/semana) | T-04 Digest |
| Mensagem fixa, sem dados externos | T-05 Lembrete |
| Resultado de sync entre sistemas | T-06 Sincronização |
| Status de N serviços/APIs | T-07 Health Check |

O template **DEVE** ser embutido diretamente no `--message` do cron job ou na
instrução do heartbeat. Nunca deixe o modelo decidir livremente o formato.

**4b — Gerar os artefatos:**
**Para OpenClaw Cron:** leia `references/cron-templates.md`
**Para Heartbeat:** leia `references/heartbeat-templates.md`
**Para Linux Cron:** gere apenas se for tarefa sem IA confirmada

Sempre gere em blocos de código prontos para copiar:
- Comando `openclaw cron add ...` completo com template Telegram embutido no `--message`
- Entrada HEARTBEAT.md (se aplicável) com template inline

---

### Passo 5 — Guia de Instalação e Validação

```bash
# 1. Criar o job
openclaw cron add [parâmetros gerados]

# 2. Confirmar criação
openclaw cron list
openclaw cron show <jobId>

# 3. Testar execução imediata
openclaw cron run <jobId> --wait

# 4. Verificar histórico
openclaw cron runs --id <jobId> --limit 5
```

---

## Regras Globais da Skill

| Regra | Detalhe |
|-------|---------|
| Sempre elicitar primeiro | Nunca gerar artefatos sem completar o Passo 1 |
| OpenClaw Cron é o padrão | Para qualquer job com IA, use `openclaw cron`, não `crontab` |
| Local → Free → Paid | Sempre avaliar modelos Ollama e OpenRouter :free antes de sugerir modelos pagos |
| `openclaw models list` obrigatório | Descobrir modelos disponíveis antes de recomendar qualquer um |
| Template Telegram obrigatório | Todo job com saída ao Telegram usa template da biblioteca `telegram-templates.md` |
| Template embutido no `--message` | O template de output DEVE estar no prompt do job, não decidido livremente pelo modelo |
| `--session isolated` por padrão | Jobs sem necessidade de histórico devem ser isolados |
| `--delete-after-run` para one-shots | Limpa o job automaticamente após execução única |
| HEARTBEAT.md não é lido por cron | Se o job de cron precisar do HEARTBEAT.md, instrua explicitamente no `--message` |

---

## Listagem e Auditoria (modo "o que tenho agendado?")

```bash
# Jobs OpenClaw Cron
openclaw cron list
openclaw cron status

# HEARTBEAT.md
cat ~/.openclaw/workspace/HEARTBEAT.md 2>/dev/null || echo "(não encontrado)"

# Linux cron (tarefas de sistema)
crontab -l 2>/dev/null || echo "(vazio)"
```

---

## Edição de Job Existente

1. Execute `openclaw cron list` para mostrar o estado atual
2. Pergunte qual job o usuário quer editar
3. Gere o comando de edição: `openclaw cron edit <jobId> --message "..." --model "..."`
4. Valide: `openclaw cron show <jobId>`

---

## Referência Rápida — Comandos CLI

```bash
openclaw cron add      # Criar novo job (alias: cron create)
openclaw cron list     # Listar todos os jobs
openclaw cron show     # Ver detalhes + rota de delivery resolvida
openclaw cron edit     # Editar job existente
openclaw cron run      # Forçar execução agora (--wait para aguardar)
openclaw cron runs     # Histórico de runs de um job
openclaw cron remove   # Deletar um job
openclaw cron status   # Status do scheduler
```
