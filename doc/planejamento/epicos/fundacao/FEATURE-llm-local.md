# Feature: Integração com Modelos LLM Locais (Ollama)

**Épico:** EP-01 — Fundação Core & Infraestrutura
**Status:** Ready
**Criado:** 2026-03-19
**Atualizado:** 2026-03-19

---

## Visão

Permitir que o agente use modelos como Llama 3 via Ollama localmente, sem depender de APIs pagas, para desenvolvimento e testes rápidos. A solução incluirá um script de configuração automatizado e um tutorial de onboarding para facilitar a adoção.

---

## Personas Impactadas

- **Desenvolvedor (Solo-Builder):** Pode iterar rapidamente sobre o comportamento do agente sem incorrer em custos de API da Google ou Anthropic durante o desenvolvimento e testes locais.

---

## User Story

> Como **desenvolvedor do Personal AI Core**, quero **configurar o agente para usar Ollama localmente** para **reduzir custos de API durante desenvolvimento e iterar mais rápido nos testes.**

---

## Critérios de Aceite (BDD)

**Cenário 1: Setup via Script e Tutorial**
- **Dado** que existe um script (`scripts/setup_local_llm.sh`) e um tutorial (`doc/guias/local-llm-setup.md`)
- **Quando** o desenvolvedor seguir o tutorial e rodar o script de configuração
- **Então** os modelos configurados (ex: `llama3`, `mistral`) ficam disponíveis localmente e prontos para uso pelo agente

**Cenário 2: Roteamento para Modelo Local**
- **Dado** que o Ollama está rodando localmente com um modelo disponível
- **Quando** o agente recebe uma mensagem e a variável `LLM_PROVIDER=ollama` está configurada
- **Então** o agente responde usando o modelo local configurado, sem chamar APIs externas (Google AI, OpenAI, etc.)

**Cenário 3: Fallback Gracioso**
- **Dado** que o Ollama não está disponível localmente
- **Quando** o agente é inicializado
- **Então** o sistema loga um erro claro e faz fallback para o provedor configurado em `LLM_PROVIDER` (padrão: `google`)

---

## Fora do Escopo

- Fine-tuning ou ajuste de pesos de modelos
- Integração com provedores cloud alternativos como Amazon Bedrock ou Azure OpenAI
- UI de seleção de modelos no dashboard React
- Avaliação comparativa (benchmarks) automatizada entre modelos

---

## Restrições Técnicas

- O backend usa **LangGraph + LangChain** — a solução deve manter compatibilidade com a interface `BaseChatModel`
- A abstração de provedor deve ser feita em `app/core/graph.py`, substituindo `ChatGoogleGenerativeAI` por uma factory function
- O modelo local deve ser configurável via variável de ambiente (ex: `LLM_PROVIDER`, `OLLAMA_MODEL`, `OLLAMA_BASE_URL`)

---

## Notas de Design

- Usar `langchain_ollama.ChatOllama` que implementa `BaseChatModel` nativamente
- A factory de LLM deve suportar: `google` (padrão), `ollama`
- Configuração via `.env`: `LLM_PROVIDER=ollama`, `OLLAMA_MODEL=llama3`, `OLLAMA_BASE_URL=http://localhost:11434`

---

## Riscos

- **Compatibilidade de tools:** Modelos locais menores podem não suportar function calling (tool use) corretamente — documentar limitações conhecidas no tutorial
- **Performance:** Modelos locais em CPU são mais lentos — não há SLA de resposta para o modo local
