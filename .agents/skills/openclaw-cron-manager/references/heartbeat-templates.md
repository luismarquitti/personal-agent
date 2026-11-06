# Templates de HEARTBEAT.md — OpenClaw

O arquivo `~/.openclaw/workspace/HEARTBEAT.md` é lido pelo agente OpenClaw para
executar tarefas periódicas em linguagem natural. Cada entrada é um item de checklist
com intervalo e instrução completa e autocontida.

Todo heartbeat que envia ao Telegram DEVE incluir um template Telegram embutido
na instrução. Use a biblioteca `telegram-templates.md` para selecionar o template
adequado ao tipo de output.

---

## Sintaxe Oficial

```markdown
- [ ] {FREQUÊNCIA}: {INSTRUÇÃO COMPLETA PARA O AGENTE}
```

**Frequências aceitas:**
```
A cada 30 minutos
A cada 1 hora / A cada 2 horas
Diariamente às 09:00
Toda segunda-feira às 08:30
Todo dia 1 do mês às 07:00
```

**Regra fundamental:** Instruções devem ser autocontidas. O agente não tem
memória entre ciclos do heartbeat. Inclua: o que fazer, onde buscar dados,
qual template usar, onde enviar.

---

## Template Base

```markdown
- [ ] {FREQUÊNCIA}: {AÇÃO PRINCIPAL}. {ONDE BUSCAR DADOS}.
  Se {CONDIÇÃO_PARA_ENVIAR}: formate usando exatamente o template abaixo e envie ao Telegram.
  {SE CONDICIONAL: Se nominal: silencioso (não enviar).}
  Sem preâmbulo. Omita seções com dados ausentes.

  Template:
  {TEMPLATE_TELEGRAM_DA_BIBLIOTECA}
```

---

## Template A: Monitoramento + Alerta Condicional (T-01)

Só envia se detectar anomalia. Usa template T-01.

```markdown
- [ ] A cada {INTERVALO}: Verifique {O_QUE_MONITORAR}.
  Se {CONDIÇÃO_DE_ALERTA}: envie ao Telegram usando exatamente o template abaixo.
  Se tudo nominal: silencioso (não enviar nada).

  Template de alerta:
  ⚠️ *ALERTA — {NOME}*
  🕐 [timestamp atual]
  • {CAMPO_1}: [valor]
  • {CAMPO_2}: [valor]
  ━━━━━━━━━━━━━━━━━━━━━
  *Motivo:* [descrição clara do problema]
  *Status:* ⚠️ ATENÇÃO
```

**Exemplo — Disco crítico:**
```markdown
- [ ] A cada 2 horas: Execute `df -h` no servidor e verifique o uso de todas
  as partições montadas. Se qualquer partição estiver acima de 85% de uso:
  envie ao Telegram usando exatamente o template abaixo. Se tudo abaixo de 85%: silencioso.

  Template de alerta:
  ⚠️ *ALERTA — DISCO CRÍTICO*
  🕐 [timestamp]
  • [mount]: [percent]% usado ([avail] livre)
  [repita para cada partição acima do limite]
  ━━━━━━━━━━━━━━━━━━━━━
  *Motivo:* Uso de disco acima de 85%
  *Status:* ⚠️ ATENÇÃO
```

---

## Template B: Relatório Periódico (T-02)

Sempre envia no horário, independente do estado. Usa template T-02.

```markdown
- [ ] {FREQUÊNCIA}: Gere um relatório de {TEMA}. Consulte {FONTE_DE_DADOS}.
  Formate usando exatamente o template abaixo. Omita seções com dados ausentes.
  Não adicione texto fora do template.

  📊 *{TÍTULO DO RELATÓRIO}*
  🕐 [timestamp] | [período coberto]

  {SEÇÃO_EMOJI} *{TÍTULO_SEÇÃO}:*
  • [campo]: [valor]

  ━━━━━━━━━━━━━━━━━━━━━
  *Status:* [✅ NOMINAL se tudo OK, ⚠️ ATENÇÃO se houver problemas]
```

**Exemplo — Resumo diário de projetos:**
```markdown
- [ ] Diariamente às 08:30: Acesse o Notion e leia o banco de dados de projetos
  ativos (Openclaw, ClinicCare, SwMaster, IntelliFinance). Para cada projeto,
  leia Status, Próximo passo e Bloqueios. Responda em português.
  Formate usando exatamente o template abaixo. Omita projetos sem dados.

  📊 *PROJETOS — [data de hoje]*
  🕐 [timestamp]

  🔹 *[nome do projeto]*: [status]
     └ Próximo: [próximo passo]
     [se bloqueio]└ ⚠️ Bloqueio: [bloqueio][/se]

  [repita para cada projeto]

  ━━━━━━━━━━━━━━━━━━━━━
  *Status:* [✅ se todos nominais, ⚠️ se houver bloqueios]
```

---

## Template C: Resumo de Lista (T-03)

Para listar itens de uma fonte externa. Usa template T-03.

```markdown
- [ ] {FREQUÊNCIA}: Consulte {FONTE} e liste {O_QUE_LISTAR}.
  Filtre por {CRITÉRIO}. Ordene por {ORDEM}. Máximo {N} itens.
  Formate usando exatamente o template abaixo. Se não houver itens: silencioso.

  📋 *{TÍTULO}*
  🕐 [timestamp]

  [N]. *[título/nome]* [emoji_status]
     └ [detalhe_1] | [detalhe_2]

  ━━━━━━━━━━━━━━━━━━━━━
  Total: [N] [tipo] | [critério de filtro]
```

**Exemplo — Issues GitHub:**
```markdown
- [ ] A cada 4 horas: Consulte os issues abertos do repositório SwMaster no GitHub
  (use $GITHUB_TOKEN). Filtre pelos criados ou atualizados nas últimas 4h.
  Ordene por data de atualização. Máximo 8 itens.
  Formate usando o template abaixo. Se não houver issues: silencioso.

  📋 *ISSUES — SwMaster*
  🕐 [timestamp]

  [N]. *[título]* ([label principal])
     └ #[número] | [autor] | atualizado há [Xh]

  ━━━━━━━━━━━━━━━━━━━━━
  Total: [N] issues atualizados nas últimas 4h
```

---

## Template D: Sincronização entre Sistemas (T-06)

Para jobs de sync. Usa template T-06.

```markdown
- [ ] {FREQUÊNCIA}: Consulte {FONTE_A} e sincronize com {DESTINO_B}.
  Para cada item em {FONTE_A} que {CONDIÇÃO}: {AÇÃO_NO_DESTINO}.
  Se houver erros: envie ao Telegram usando o template abaixo.
  Se tudo sincronizado com sucesso: silencioso.

  🔄 *SYNC — [origem] → [destino]*
  🕐 [timestamp]
  ✅ Criados: [N]
  🔄 Atualizados: [N]
  ⏭️ Ignorados: [N]
  [se erros]🔴 Erros: [N]
  ━━━━━━━━━━━━━━━━━━━━━
  ⚠️ *Erros:* [lista de erros][/se]
```

---

## Template E: Lembrete Fixo (T-05)

Para lembretes sem dados externos. Usa template T-05.

```markdown
- [ ] {FREQUÊNCIA}: Envie ao Telegram usando exatamente o template abaixo.

  {EMOJI} *{TÍTULO}*
  {CORPO_FIXO}
  [se ação requerida]
  👉 {AÇÃO_ESPERADA}
  [/se]
```

**Exemplo — Checklist de standup:**
```markdown
- [ ] Toda segunda-feira às 08:45: Envie ao Telegram usando exatamente o template:

  🎯 *STANDUP — Segunda-feira*
  Hora de preparar o daily!

  • O que fiz na última semana?
  • O que vou fazer hoje?
  • Algum bloqueio?

  👉 Responda no grupo antes das 09:00
```

---

## Template F: Referência a Skill Interna

Para lógica complexa, referencie uma skill interna. Inclua sempre o template
de output Telegram na skill interna (não no heartbeat).

```markdown
- [ ] {FREQUÊNCIA}: Execute a skill `{nome_skill}`. Contexto: {CONTEXTO_RESUMIDO}.
  A skill define o template de output e canal de envio.
```

---

## Estrutura Recomendada do HEARTBEAT.md Completo

```markdown
# OpenClaw Heartbeat

<!-- ══ MONITORAMENTO ══ -->
- [ ] A cada 1 hora: [job com template T-01]
- [ ] A cada 2 horas: [job com template T-01]

<!-- ══ RELATÓRIOS DIÁRIOS ══ -->
- [ ] Diariamente às 08:30: [job com template T-02]
- [ ] Diariamente às 09:00: [job com template T-02]

<!-- ══ LISTAS / RESUMOS ══ -->
- [ ] A cada 4 horas: [job com template T-03]

<!-- ══ SINCRONIZAÇÕES ══ -->
- [ ] A cada 6 horas: [job com template T-06]

<!-- ══ LEMBRETES FIXOS ══ -->
- [ ] Toda sexta-feira às 17:00: [job com template T-05]
```

---

## Boas Práticas

| Prática | Motivo |
|---------|--------|
| Template Telegram obrigatório na instrução | Garante formatação consistente |
| "Silencioso se nominal" para monitoramentos | Evita spam no Telegram |
| Contexto completo na instrução | Agente não tem memória entre ciclos |
| Agrupar por categoria com comentários | Facilita manutenção |
| Máximo N itens explícito em listas | Evita mensagens longas demais |
| Skill interna para lógica complexa | Mantém HEARTBEAT.md legível |
