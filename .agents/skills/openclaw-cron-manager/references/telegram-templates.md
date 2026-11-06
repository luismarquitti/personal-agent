# Templates Padrão de Mensagens Telegram — OpenClaw Jobs

Todos os jobs e heartbeats que enviam ao Telegram DEVEM usar um template desta
biblioteca. O template deve ser embutido diretamente no `--message` do job ou
na instrução do HEARTBEAT.md para garantir consistência de formatação.

---

## Regras Gerais de Formatação Telegram

- OpenClaw envia por padrão em **Markdown** (parse_mode do Telegram)
- `*texto*` → **negrito**
- `_texto_` → _itálico_
- `` `código` `` → `inline code`
- Use `━━━━━━━━━━━━` como separador de seções
- Emojis de status: `✅` nominal | `⚠️` atenção | `🔴` crítico | `⬜` N/A
- Omita seções inteiras quando os dados forem null/ausentes
- Nunca adicione texto fora do template (sem preâmbulo, sem "aqui está:")
- Máximo ~4000 caracteres por mensagem (limite do Telegram)

---

## Biblioteca de Templates

### T-01: Alerta de Anomalia (disparo condicional)

Use quando: job monitora algo e só deve enviar SE houver problema.

```
⚠️ *ALERTA — {NOME_DO_JOB}*
🕐 {timestamp}

{CAMPO_1}: {valor_1}
{CAMPO_2}: {valor_2}

━━━━━━━━━━━━━━━━━━━━━
*Motivo:* {DESCRIÇÃO_DA_ANOMALIA}
*Status:* ⚠️ ATENÇÃO
```

**Instrução para o prompt:**
```
Se {CONDIÇÃO_DE_ALERTA}: envie ao Telegram usando exatamente o template T-01:

⚠️ *ALERTA — {NOME_DO_JOB}*
🕐 [timestamp atual]
[campos relevantes da anomalia]
━━━━━━━━━━━━━━━━━━━━━
*Motivo:* [descrição clara do problema]
*Status:* ⚠️ ATENÇÃO

Se tudo nominal: não envie nada (silencioso).
```

---

### T-02: Relatório Periódico

Use quando: job gera relatório em horário fixo, independente do estado.

```
📊 *{TÍTULO DO RELATÓRIO}*
🕐 {timestamp} | {PERÍODO_COBERTO}

{SEÇÃO_1_EMOJI} *{TÍTULO_SEÇÃO_1}:*
• {item}: {valor}
• {item}: {valor}

{SEÇÃO_2_EMOJI} *{TÍTULO_SEÇÃO_2}:*
• {item}: {valor}

━━━━━━━━━━━━━━━━━━━━━
*Status:* ✅ NOMINAL / ⚠️ ATENÇÃO
```

**Instrução para o prompt:**
```
Formate o relatório usando exatamente o template abaixo. Omita seções com
dados ausentes. Não adicione texto fora do template.

📊 *{TÍTULO}*
🕐 [timestamp] | [período]

[seções conforme dados disponíveis]

━━━━━━━━━━━━━━━━━━━━━
*Status:* [✅ NOMINAL se tudo OK, ⚠️ ATENÇÃO se houver problemas]
```

---

### T-03: Resumo de Lista (issues, commits, tasks)

Use quando: job lista itens de uma fonte (GitHub, Notion, etc.).

```
📋 *{TÍTULO DA LISTA}*
🕐 {timestamp}

{para cada item — máximo N}
{N}. *{título/nome}* {emoji_status}
   └ {detalhe_1} | {detalhe_2}
{/para}

━━━━━━━━━━━━━━━━━━━━━
Total: {N} {TIPO} | {CRITÉRIO_DE_FILTRO}
```

**Instrução para o prompt:**
```
Liste os itens usando exatamente o template abaixo. Máximo {N} itens
(priorize os mais {CRITÉRIO}). Omita campos ausentes. Sem preâmbulo.

📋 *{TÍTULO}*
🕐 [timestamp]

[lista numerada dos itens]

━━━━━━━━━━━━━━━━━━━━━
Total: [N] [tipo] | [critério usado]
```

---

### T-04: Digest Diário / Weekly Wrap-up

Use quando: job consolida informações de um período (dia, semana).

```
📅 *{TÍTULO} — {DATA_OU_PERÍODO}*

{BLOCO_1_EMOJI} *{CATEGORIA_1}:*
{conteúdo da categoria 1}

{BLOCO_2_EMOJI} *{CATEGORIA_2}:*
{conteúdo da categoria 2}

{se houver itens de atenção}
⚠️ *Requer atenção:*
• {item de atenção 1}
• {item de atenção 2}
{/se}

━━━━━━━━━━━━━━━━━━━━━
{FRASE_RESUMO_DO_DIA_OU_SEMANA}
```

---

### T-05: Lembrete / Sistema de Eventos

Use quando: job envia mensagem fixa de lembrete (sem dados externos).

```
{EMOJI} *{TÍTULO DO LEMBRETE}*

{CORPO_DA_MENSAGEM}

{se houver ação requerida}
👉 {AÇÃO_ESPERADA}
{/se}
```

---

### T-06: Resultado de Sincronização / Integração

Use quando: job sincroniza dados entre sistemas e reporta o resultado.

```
🔄 *SYNC — {ORIGEM} → {DESTINO}*
🕐 {timestamp}

✅ Criados: {N}
🔄 Atualizados: {N}
⏭️ Ignorados: {N}
{se erros}🔴 Erros: {N}{/se}

{se erros}
━━━━━━━━━━━━━━━━━━━━━
⚠️ *Erros:*
{lista de erros}
{/se}
```

---

### T-07: Status de Saúde (Multi-serviço)

Use quando: job verifica status de múltiplos serviços/endpoints.

```
🩺 *HEALTH CHECK — {ESCOPO}*
🕐 {timestamp}

{para cada serviço}
{emoji_status} {nome}: {status_descritivo}
{/para}

━━━━━━━━━━━━━━━━━━━━━
*Status Geral:* ✅ NOMINAL / ⚠️ ATENÇÃO / 🔴 CRÍTICO
```

---

## Como Embutir o Template no Job

### Em `openclaw cron add --message`:

O `--message` deve conter a instrução completa + template:

```bash
openclaw cron add \
  --name "github-issues-daily" \
  --cron "0 9 * * 1-5" \
  --tz "America/Sao_Paulo" \
  --session isolated \
  --message "Consulte os issues abertos do repositório SwMaster no GitHub.
Filtre pelos criados ou atualizados nas últimas 24h.
Ordene por data de criação (mais recente primeiro).
Formate usando exatamente o template abaixo. Máximo 10 itens. Omita se não houver issues. Sem preâmbulo.

📋 *ISSUES — SwMaster*
🕐 [timestamp]

[lista numerada: N. *título* (label)
   └ #número | autor | criado há Xh]

━━━━━━━━━━━━━━━━━━━━━
Total: [N] issues abertos nas últimas 24h" \
  --model "openrouter/meta-llama/llama-3.3-70b-instruct:free" \
  --announce \
  --channel telegram \
  --to "{CHAT_ID}"
```

### Em HEARTBEAT.md:

A instrução deve incluir o template inline:

```markdown
- [ ] Diariamente às 09:00: Verifique o status dos containers Docker no servidor.
  Formate usando exatamente o template abaixo e envie ao Telegram.
  Se todos nominais: mensagem silenciosa (não enviar).
  Template (usar apenas se houver containers DOWN):
  ```
  🩺 *DOCKER STATUS*
  🕐 [timestamp]
  [lista de containers com problema: 🔴 nome: stopped]
  ━━━━━━━━━━━━━━━━━━━━━
  *Status Geral:* ⚠️ ATENÇÃO — [N] container(s) parado(s)
  ```
```

---

## Seleção Rápida de Template

| Situação | Template |
|----------|----------|
| Só envia se detectar problema | T-01 Alerta |
| Relatório sempre no horário | T-02 Relatório Periódico |
| Lista de itens (issues, PRs, tasks) | T-03 Resumo de Lista |
| Resumo de um período (dia/semana) | T-04 Digest |
| Mensagem fixa, sem dados externos | T-05 Lembrete |
| Resultado de sync entre sistemas | T-06 Sincronização |
| Status de N serviços/APIs | T-07 Health Check |
