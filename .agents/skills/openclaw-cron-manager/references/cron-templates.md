# Templates de Cron Job — OpenClaw Native CLI

O OpenClaw tem seu próprio sistema de agendamento integrado ao Gateway.
NÃO use `crontab` para jobs do OpenClaw — use `openclaw cron add`.

---

## Referência de Tipos de Schedule

| Flag | Formato | Exemplo |
|------|---------|---------|
| `--at` | ISO 8601 ou relativo (`20m`, `2h`) | `--at "2026-02-01T09:00:00Z"` |
| `--every` | Intervalo fixo | `--every 1h`, `--every 30m` |
| `--cron` | Expressão 5 ou 6 campos | `--cron "0 9 * * *"` |

> **Atenção — OR logic:** quando day-of-month E day-of-week são não-wildcard, o
> OpenClaw usa OR (Vixie padrão). `0 9 15 * 1` dispara em todo dia 15 E toda
> segunda. Para exigir ambos, use o modificador `+`: `0 9 15 * +1`.

---

## Referência de Execution Styles (--session)

| Valor | Contexto | Melhor para |
|-------|----------|-------------|
| `main` | Lane dedicada do heartbeat | Lembretes, system events |
| `isolated` | Sessão nova a cada run | Relatórios, tarefas em background |
| `current` | Vinculado à sessão atual na criação | Trabalho recorrente com contexto |
| `session:custom-id` | Sessão nomeada persistente | Workflows que acumulam histórico |

---

## Template A: Job Isolado com Entrega no Telegram

> Para o `--message`, sempre embuta um template Telegram da biblioteca
> `telegram-templates.md`. Consulte o `prompt-optimizer.md` para `--model`.

```bash
openclaw cron add \
  --name "{NOME_DO_JOB}" \
  --cron "{EXPRESSÃO_CRON}" \
  --tz "America/Sao_Paulo" \
  --session isolated \
  --message "{INSTRUÇÃO + TEMPLATE_TELEGRAM_EMBUTIDO}" \
  --model "{MODELO_SELECIONADO_VIA_PROMPT_OPTIMIZER}" \
  --announce \
  --channel telegram \
  --to "{CHAT_ID}"
```

**Exemplo — Resumo diário de projetos às 08:30 (template T-02):**
```bash
openclaw cron add \
  --name "resumo-projetos" \
  --cron "30 8 * * 1-5" \
  --tz "America/Sao_Paulo" \
  --session isolated \
  --message "Acesse o Notion e leia o banco de dados de projetos ativos
(Openclaw, ClinicCare, SwMaster, IntelliFinance). Para cada projeto, leia
Status, Próximo passo e Bloqueios. Responda em português.
Formate usando exatamente o template abaixo. Omita projetos sem dados. Sem preâmbulo.

📊 *PROJETOS — [data de hoje]*
🕐 [timestamp]

🔹 *[nome do projeto]*: [status]
   └ Próximo: [próximo passo]
   [se bloqueio]└ ⚠️ Bloqueio: [bloqueio][/se]

[repita para cada projeto]

━━━━━━━━━━━━━━━━━━━━━
*Status:* ✅ NOMINAL / ⚠️ ATENÇÃO" \
  --model "ollama/qwen2.5:7b" \
  --announce \
  --channel telegram \
  --to "{CHAT_ID}"
```

---

## Template B: Job de Monitoramento com Alerta Condicional

> Use template T-01 da biblioteca `telegram-templates.md`.
> Modelo: avalie via `prompt-optimizer.md` — Tier 0 (local) geralmente suficiente.

```bash
openclaw cron add \
  --name "{NOME}-monitor" \
  --every {INTERVALO} \
  --session isolated \
  --message "Verifique {O_QUE_MONITORAR}.
Se {CONDIÇÃO_DE_ALERTA}: envie ao Telegram usando exatamente o template abaixo.
Se tudo nominal: não envie nada (silencioso).

⚠️ *ALERTA — {NOME}*
🕐 [timestamp]
• {CAMPO}: [valor]
━━━━━━━━━━━━━━━━━━━━━
*Motivo:* [descrição do problema]
*Status:* ⚠️ ATENÇÃO" \
  --model "{MODELO_VIA_PROMPT_OPTIMIZER}" \
  --announce \
  --channel telegram \
  --to "{CHAT_ID}"
```

---

## Template C: One-shot / Reminder

```bash
openclaw cron add \
  --name "{NOME}" \
  --at "{TIMESTAMP_ISO_OU_RELATIVO}" \
  --session main \
  --system-event "{TEXTO_DO_LEMBRETE}" \
  --wake now \
  --delete-after-run
```

**Exemplo:**
```bash
openclaw cron add \
  --name "lembrete-deploy" \
  --at "30m" \
  --session main \
  --system-event "Lembrete: verificar resultado do deploy do ClinicCare." \
  --wake now \
  --delete-after-run
```

---

## Template D: Job com Análise Profunda (Tier 1/2/3)

> Para análises que exigem raciocínio. Consulte `prompt-optimizer.md` —
> considere `ollama/deepseek-r1:7b` local ou `openrouter/deepseek/deepseek-r1:free`
> antes de modelos pagos. Use template T-02 ou T-04 para o output.

```bash
openclaw cron add \
  --name "{NOME}-deep" \
  --cron "0 6 * * 1" \
  --tz "America/Sao_Paulo" \
  --session isolated \
  --message "{INSTRUÇÃO_ANALÍTICA + TEMPLATE_T02_OU_T04_EMBUTIDO}" \
  --model "{MODELO_TIER_1_OU_2_VIA_PROMPT_OPTIMIZER}" \
  --thinking high \
  --announce \
  --channel telegram \
  --to "{CHAT_ID}"
```

---

## Template E: Job com Saída via Webhook

```bash
openclaw cron add \
  --name "{NOME}-webhook" \
  --cron "{SCHEDULE}" \
  --session isolated \
  --message "{INSTRUÇÃO_COM_OUTPUT_JSON_ESTRUTURADO}" \
  --model "{MODELO_VIA_PROMPT_OPTIMIZER}"
  --webhook "https://{SEU_ENDPOINT}/openclaw/cron"
```

> Webhook e chat delivery são mutuamente exclusivos — não combine `--webhook`
> com `--announce`/`--channel`/`--to`.

---

## Template F: Job com Sessão Persistente (Histórico Acumulado)

Para jobs que devem manter contexto entre execuções. Use template T-04 para output.

```bash
openclaw cron add \
  --name "standup-diario" \
  --cron "45 8 * * 1-5" \
  --tz "America/Sao_Paulo" \
  --session "session:standup" \
  --message "Daily standup. Baseado no contexto desta sessão, consolide:
o que foi concluído desde o último standup, prioridades de hoje, bloqueios.
Responda em português. Formate usando exatamente o template abaixo. Sem preâmbulo.

📅 *STANDUP — [data de hoje]*

✅ *Concluído:*
[lista do que foi feito]

🎯 *Hoje:*
[prioridades do dia]

[se bloqueio]⚠️ *Bloqueios:*
[lista de bloqueios][/se]

━━━━━━━━━━━━━━━━━━━━━
[frase resumo do estado atual]" \
  --model "{MODELO_VIA_PROMPT_OPTIMIZER}" \
  --announce \
  --channel telegram \
  --to "{CHAT_ID}"
```

---

## Gerenciamento de Jobs (CLI Completa)

```bash
# Listar todos os jobs
openclaw cron list

# Ver detalhes de um job específico
openclaw cron show <jobId>

# Editar um job existente
openclaw cron edit <jobId> --message "Prompt atualizado" --model "sonnet"

# Forçar execução imediata
openclaw cron run <jobId>

# Forçar e aguardar conclusão
openclaw cron run <jobId> --wait --wait-timeout 5m

# Ver histórico de runs
openclaw cron runs --id <jobId> --limit 20

# Remover um job
openclaw cron remove <jobId>

# Status geral do cron
openclaw cron status
```

---

## Quando usar Linux cron (`crontab`) — casos residuais

Linux cron ainda faz sentido **fora do ecossistema OpenClaw** para:
- Tarefas puramente de sistema sem IA (backup de arquivos, limpeza de logs)
- Jobs que precisam rodar mesmo se o Gateway do OpenClaw estiver offline
- Triggers externos que chamam o Gateway via webhook HTTP

```bash
# Exemplo: backup diário sem IA (legítimo usar crontab)
0 2 * * * /home/luis/scripts/backup_proxmox.sh >> /var/log/backup.log 2>&1

# Exemplo: trigger externo para o Gateway do OpenClaw via webhook
*/5 * * * * curl -sf -X POST http://127.0.0.1:18789/hooks/agent \
  -H 'Authorization: Bearer {TOKEN}' \
  -H 'Content-Type: application/json' \
  -d '{"message":"Check disk health","name":"disk-check"}' \
  >> /var/log/openclaw-webhook.log 2>&1
```

---

## Troubleshooting Rápido

```bash
# Cron não disparou?
openclaw status
openclaw gateway status
openclaw cron status
openclaw cron runs --id <jobId> --limit 10
openclaw logs --follow
openclaw doctor
```

Causas comuns: Gateway não está rodando continuamente; `cron.enabled: false`;
timezone errada (`--tz` vs timezone do host); job com `--due` não estava vencido.
