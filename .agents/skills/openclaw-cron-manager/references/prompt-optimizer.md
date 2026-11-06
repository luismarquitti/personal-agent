# Otimizador de Modelo e Prompt — OpenClaw Jobs

Guia para selecionar o melhor modelo disponível e estruturar o prompt mais
eficiente para cada job. Prioridade: **local → free cloud → paid cloud**.

---

## Passo 0 — Descobrir os Modelos Disponíveis

Antes de recomendar um modelo, sempre execute ou peça ao usuário para executar:

```bash
# Lista todos os modelos configurados no OpenClaw
openclaw models list

# Alternativa: ver providers configurados
cat ~/.openclaw/config.json | jq '.providers // .models // .'
# ou
openclaw config show | grep -A 5 "provider\|model"
```

Identifique quais provedores estão ativos:
- **Ollama** (local) → modelos sem custo e sem latência de rede
- **OpenRouter** (cloud, gratuito possível) → modelos free via `openrouter/...`
- **Anthropic** (cloud, pago) → Claude family
- **OpenAI** (cloud, pago) → GPT/o-series
- **Gemini** (cloud, pago/gratuito) → Gemini family
- **Groq** (cloud, rápido/barato) → Llama, Gemma via Groq
- **Outros** → conforme configuração local

---

## Hierarquia de Seleção (ordem de preferência)

```
Tier 0 — Local (Ollama)        → custo zero, sem latência de rede, privacidade total
Tier 1 — Free Cloud            → custo zero, latência de rede, limites de RPM/dia
Tier 2 — Paid Cloud (pequeno)  → custo baixo, alta disponibilidade
Tier 3 — Paid Cloud (médio)    → custo médio, alta capacidade
Tier 4 — Paid Cloud (poderoso) → custo alto, máximo de raciocínio
```

**Regra:** desça o mínimo necessário na hierarquia para resolver o problema.
Jobs automáticos devem usar Tier 0 ou Tier 1 sempre que a tarefa permitir.

---

## Referência de Modelos por Tier e Tarefa

### Tier 0 — Local (Ollama)

| Modelo Ollama | Parâmetros | Adequado para |
|---------------|-----------|---------------|
| `ollama/llama3.2` | 3B | Formatação simples, mapeamento de dados, lembretes |
| `ollama/llama3.2:1b` | 1B | Templates 100% fixos, formatação trivial |
| `ollama/qwen2.5:7b` | 7B | Sumarização, análise leve, múltiplos idiomas |
| `ollama/qwen2.5:14b` | 14B | Análise técnica, correlação de dados |
| `ollama/gemma3:4b` | 4B | Formatação + lógica condicional simples |
| `ollama/mistral:7b` | 7B | Análise geral, síntese de texto |
| `ollama/phi4:14b` | 14B | Raciocínio técnico, análise de código/logs |
| `ollama/deepseek-r1:7b` | 7B | Raciocínio estruturado, análise com cadeia de pensamento |

> Verifique os modelos baixados com `ollama list`. Se o modelo desejado não
> estiver disponível: `ollama pull <modelo>`.

### Tier 1 — Free Cloud (OpenRouter)

| Modelo | String API | Adequado para |
|--------|-----------|---------------|
| Llama 3.3 70B | `openrouter/meta-llama/llama-3.3-70b-instruct:free` | Análise, sumarização, boa capacidade geral |
| Gemma 3 27B | `openrouter/google/gemma-3-27b-it:free` | Análise técnica, formatação avançada |
| Qwen 2.5 72B | `openrouter/qwen/qwen-2.5-72b-instruct:free` | Multilíngue, análise de dados |
| DeepSeek R1 | `openrouter/deepseek/deepseek-r1:free` | Raciocínio complexo, análise profunda |
| Phi-4 Reasoning | `openrouter/microsoft/phi-4-reasoning:free` | Raciocínio técnico |

> Modelos `:free` têm limites de RPM (requests/minute) e RPD (requests/day).
> Para jobs de alta frequência (< 30 min), prefira Tier 0.

### Tier 2 — Paid Cloud (pequeno / barato)

| Modelo | String API | Adequado para |
|--------|-----------|---------------|
| Claude Haiku 4 | `claude-haiku-4-5-20251001` | Formatação, mapeamento, templates fixos |
| Gemini 2.0 Flash | `gemini/gemini-2.0-flash` | Rápido, barato, boa capacidade geral |
| GPT-4o mini | `openai/gpt-4o-mini` | Análise leve, estruturado |
| Llama 3.3 70B (pago) | `openrouter/meta-llama/llama-3.3-70b-instruct` | Alta capacidade sem limite de taxa |
| Groq Llama 3.3 70B | `groq/llama-3.3-70b-versatile` | Ultra-rápido, análise geral |

### Tier 3 — Paid Cloud (médio)

| Modelo | String API | Adequado para |
|--------|-----------|---------------|
| Claude Sonnet 4 | `claude-sonnet-4-6` | Análise profunda, síntese multi-fonte |
| GPT-4o | `openai/gpt-4o` | Análise complexa, raciocínio |
| Gemini 2.5 Pro | `gemini/gemini-2.5-pro` | Análise avançada, contexto longo |

### Tier 4 — Paid Cloud (poderoso)

| Modelo | String API | Quando usar |
|--------|-----------|-------------|
| Claude Opus 4 | `claude-opus-4-6` | Decisões críticas — evitar em automações |
| o3 / o4 | `openai/o3` | Raciocínio máximo — raramente em jobs |

---

## Matriz de Decisão: Complexidade × Modelo Recomendado

| Tipo de Job | Tier Mínimo | Modelo Local Preferido | Fallback Free Cloud | Fallback Pago |
|-------------|-------------|----------------------|--------------------|----|
| Formatar JSON → Telegram (template fixo) | **0** | `ollama/llama3.2` | `openrouter/google/gemma-3-27b-it:free` | `claude-haiku-4-5-20251001` |
| Mapeamento de dados / alerta condicional | **0** | `ollama/qwen2.5:7b` | `openrouter/meta-llama/llama-3.3-70b-instruct:free` | `claude-haiku-4-5-20251001` |
| Sumarização de lista (issues, commits) | **0** | `ollama/qwen2.5:7b` | `openrouter/meta-llama/llama-3.3-70b-instruct:free` | `claude-haiku-4-5-20251001` |
| Relatório com métricas agregadas | **0/1** | `ollama/qwen2.5:14b` | `openrouter/qwen/qwen-2.5-72b-instruct:free` | `gemini/gemini-2.0-flash` |
| Análise técnica de logs / erros | **0/1** | `ollama/phi4:14b` | `openrouter/microsoft/phi-4-reasoning:free` | `claude-sonnet-4-6` |
| Síntese de múltiplas fontes | **1/2** | `ollama/deepseek-r1:7b` | `openrouter/deepseek/deepseek-r1:free` | `claude-sonnet-4-6` |
| Análise de tendências históricas | **1/2** | `ollama/qwen2.5:14b` | `openrouter/meta-llama/llama-3.3-70b-instruct:free` | `claude-sonnet-4-6` |
| Priorizar tasks / próximos passos | **1/2** | `ollama/deepseek-r1:7b` | `openrouter/deepseek/deepseek-r1:free` | `claude-sonnet-4-6` |
| Raciocínio complexo / decisão crítica | **3** | _(local insuficiente)_ | `openrouter/deepseek/deepseek-r1:free` | `claude-sonnet-4-6` |

---

## Como Recomendar ao Usuário

1. Execute `openclaw models list` para ver o que está disponível
2. Identifique os modelos locais (Ollama) instalados → **sempre priorize**
3. Verifique se OpenRouter está configurado → use modelos `:free` quando possível
4. Apenas sugira modelos pagos se os tiers anteriores forem insuficientes para a tarefa
5. Apresente: modelo recomendado + fallback + justificativa

**Formato de apresentação:**
```
✅ Recomendado: ollama/qwen2.5:7b (local, custo zero)
🔄 Fallback:    openrouter/meta-llama/llama-3.3-70b-instruct:free
💰 Se precisar: claude-haiku-4-5-20251001
Justificativa: tarefa de formatação simples — modelo 7B local é suficiente.
```

---

## Estratégias de Prompt por Complexidade

### Estratégia 1: Mapeamento Determinístico (Tier 0/1)

Quando o output é 100% derivado do input. Zero inferência.

```
Você é um formatador determinístico.
Regras rígidas:
- Mapeie APENAS campos presentes na entrada
- Omita seções com valores null, vazios ou ausentes
- Não infira, estime ou adicione dados não presentes
- Responda APENAS com a mensagem formatada, sem preâmbulo
- Use exatamente o template abaixo

[TEMPLATE]
{TEMPLATE COMPLETO}
[/TEMPLATE]
```

**Tokens estimados:** system ~150t + input ~300-800t + output ~100-300t = **~550-1250t/run**

---

### Estratégia 2: Análise com Saída Estruturada (Tier 0/1)

Quando o input é semi-estruturado mas o output segue template fixo.

```
Você é um analista de {DOMÍNIO}.
Tarefa: {TAREFA EM 1 FRASE}.
Entrada: {DESCRIÇÃO DO INPUT}.

Regras:
- Siga o template de saída abaixo exatamente
- Máximo {N} itens por seção (priorize os mais {CRITÉRIO})
- Se {CAMPO} estiver ausente: omita a seção
- Resposta apenas com a mensagem formatada, sem preâmbulo

[TEMPLATE]
{TEMPLATE}
[/TEMPLATE]
```

**Tokens estimados:** system ~250t + input ~500-2000t + output ~200-500t = **~950-2750t/run**

---

### Estratégia 3: Síntese Multi-Fonte (Tier 1/2)

Quando dados de múltiplas fontes precisam ser correlacionados.

```
Você é o assistente de operações do Luis.
Objetivo: {OBJETIVO EM 1 FRASE}.

Fontes no payload:
- {FONTE_A}: {o que contém}
- {FONTE_B}: {o que contém}

Contexto mínimo: {APENAS O NECESSÁRIO}.

Saída obrigatória — use exatamente este template:
[TEMPLATE]
{TEMPLATE}
[/TEMPLATE]

Se uma fonte retornar erro: sinalize com ⚠️ e continue com as demais.
Resposta apenas com a mensagem formatada.
```

**Tokens estimados:** system ~400t + input ~1000-5000t + output ~300-800t = **~1700-6200t/run**

---

## Otimizações Gerais

| Técnica | Quando aplicar | Economia estimada |
|---------|---------------|-------------------|
| Compressão do payload JSON | Sempre (remover campos desnecessários via `jq`) | 60-80% do input |
| Template embutido no prompt | Sempre | Elimina mensagens de follow-up |
| `--light-context` no cron | Jobs que não precisam do workspace | Reduz bootstrap |
| Modelo local (Ollama) | Quando suficiente para a tarefa | 100% do custo cloud |
| Modelo free (OpenRouter) | Quando local insuficiente | 100% do custo cloud |
| Frequência adequada | Não agendar mais frequente que o necessário | Reduz runs totais |

---

## Checklist antes de Finalizar um Job

- [ ] `openclaw models list` executado e modelos disponíveis identificados?
- [ ] Modelo mais leve suficiente para a tarefa escolhido?
- [ ] Payload comprimido (apenas campos necessários via `jq`)?
- [ ] Template de output embutido no `--message`?
- [ ] Tier local ou free cloud avaliado antes de sugerir modelo pago?
- [ ] Frequência do job justificada (não mais frequente que o necessário)?
- [ ] `--light-context` avaliado para jobs simples?
