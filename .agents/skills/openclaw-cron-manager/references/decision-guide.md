# Guia de Decisão: OpenClaw Cron vs Heartbeat vs Linux Cron

## Os três mecanismos — visão geral

| Mecanismo | Sistema | Gerenciado via | Melhor para |
|-----------|---------|---------------|-------------|
| **OpenClaw Cron** | Gateway interno | `openclaw cron add` | Jobs recorrentes com LLM, entrega nativa |
| **Heartbeat** | Main session periódica | `~/.openclaw/workspace/HEARTBEAT.md` + config | Tarefas contínuas da sessão principal |
| **Linux Cron** | Sistema operacional | `crontab` | Tarefas sem IA, backups, fora do Gateway |

> **Regra geral:** qualquer job que envolva IA + entrega → **OpenClaw Cron nativo**.
> Linux cron é o último recurso, para tarefas puramente de sistema.

---

## Diferenças-chave: OpenClaw Cron vs Heartbeat

| Critério | OpenClaw Cron | Heartbeat |
|----------|--------------|-----------|
| Configuração | `openclaw cron add` (CLI) | Entrada em `HEARTBEAT.md` (texto) |
| Sessão | Isolated, main, custom por job | Main session contínua |
| Contexto entre runs | Opcional (`session:custom-id`) | Inerente (mesma sessão) |
| Gerenciamento de estado | SQLite (histórico, retry, status) | Sem histórico estruturado |
| Delivery | Canal configurável por job | Depende das instruções no prompt |
| Retry automático | ✅ Backoff configurável | ❌ |
| Timeout por run | ✅ | ❌ |
| Run history | `openclaw cron runs --id` | ❌ |
| Override de modelo | ✅ Por job | Via instrução no texto |
| HEARTBEAT.md | **Não lido automaticamente** por cron | Lido pelo heartbeat principal |

> **Nota importante da documentação oficial:** Jobs de cron no modo `main session`
> NÃO incluem automaticamente a instrução "Read HEARTBEAT.md". Se um job de cron
> precisa consultar o HEARTBEAT.md, isso deve ser explícito no prompt do job.

---

## Árvore de Decisão

```
É uma tarefa recorrente ou agendada?
│
├── Puramente de sistema (sem IA)?
│   ex: backup, limpeza de logs, rsync
│   └── → [LINUX CRON] crontab -e
│
├── Precisa de IA + execução isolada + histórico de runs?
│   ex: relatório, monitoramento, análise periódica
│   └── → [OPENCLAW CRON] openclaw cron add --session isolated
│
├── Precisa de IA e acumula contexto entre runs?
│   ex: standup diário que referencia o dia anterior
│   └── → [OPENCLAW CRON] openclaw cron add --session session:custom-id
│
├── É um lembrete one-shot ou system event para a sessão principal?
│   ex: "daqui a 30min, verificar o deploy"
│   └── → [OPENCLAW CRON] openclaw cron add --at "30m" --session main --delete-after-run
│
└── É uma tarefa contínua/ambient da sessão principal?
    ex: checklist que o agente principal já sabe seguir
    └── → [HEARTBEAT.md] entrada no arquivo de heartbeat
```

---

## Perfis de Uso

### Perfil A: OpenClaw Cron — Isolated (mais comum)
**Quando:** relatórios periódicos, monitoramento com alerta, sumarizações, análises.

**Características:**
- Sessão nova a cada execução (sem herdar contexto anterior)
- Delivery direto ao Telegram/Slack/Discord/webhook
- Histórico completo de runs
- Override de modelo por job

```bash
openclaw cron add \
  --name "exemplo" \
  --cron "0 9 * * *" \
  --tz "America/Sao_Paulo" \
  --session isolated \
  --message "..." \
  --model "claude-haiku-4-5-20251001" \
  --announce --channel telegram --to "{CHAT_ID}"
```

---

### Perfil B: OpenClaw Cron — Custom Session (contexto acumulado)
**Quando:** standups, revisões semanais, qualquer job que se beneficia de "lembrar" runs anteriores.

```bash
openclaw cron add \
  --name "standup" \
  --cron "45 8 * * 1-5" \
  --tz "America/Sao_Paulo" \
  --session "session:standup-luis" \
  --message "..." \
  --model "claude-sonnet-4-6" \
  --announce --channel telegram --to "{CHAT_ID}"
```

---

### Perfil C: HEARTBEAT.md (Heartbeat da sessão principal)
**Quando:** tarefas ambient que o agente principal deve executar no ciclo do heartbeat; sem necessidade de histórico estruturado ou retry automático.

**Formato:**
```markdown
- [ ] A cada {intervalo}: {instrução completa e autocontida para o agente}
- [ ] Diariamente às {HH:MM}: {instrução}
```

**Atenção:** o heartbeat lê este arquivo periodicamente. Inclua o contexto
completo na instrução — o agente não tem memória entre ciclos do heartbeat.

---

### Perfil D: Linux Cron (residual)
**Quando:** tarefas 100% de sistema sem envolvimento do Gateway OpenClaw.

```bash
# Legítimo: backup às 2h, sem IA
0 2 * * * /home/luis/scripts/backup.sh >> /var/log/backup.log 2>&1
```

---

## Casos de Uso → Mecanismo Recomendado

| Caso de Uso | Mecanismo |
|-------------|-----------|
| Resumo diário de commits GitHub | OpenClaw Cron (isolated) |
| Alerta de CPU/RAM acima de threshold | OpenClaw Cron (isolated) |
| Relatório semanal IntelliFinance | OpenClaw Cron (isolated) |
| Standup diário com histórico | OpenClaw Cron (session:standup) |
| Reminder one-shot "em 30 min" | OpenClaw Cron (--at + main) |
| Checklist ambient do agente principal | HEARTBEAT.md |
| Backup de arquivos do Proxmox | Linux Cron (sem IA) |
| Limpeza de logs antigos | Linux Cron (sem IA) |
| Sync Notion ↔ GitHub issues | OpenClaw Cron (isolated) |
| Relatório diário de projetos | OpenClaw Cron (isolated) |
| Análise semanal de tendências | OpenClaw Cron (isolated, sonnet) |
| Trigger externo via HTTP → Gateway | Linux Cron → webhook HTTP do Gateway |
