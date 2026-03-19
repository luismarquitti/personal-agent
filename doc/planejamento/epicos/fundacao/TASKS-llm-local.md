# Tasks: Integração com Modelos LLM Locais (Ollama)

**Feature:** FEATURE-llm-local.md
**Épico:** EP-01 — Fundação Core & Infraestrutura
**Criado:** 2026-03-19

---

## Fase 1: Fundação — Abstração do Provedor LLM

- [ ] **1.1** Criar `app/core/llm_factory.py` com uma função `get_llm()` que retorna um `BaseChatModel` com base na variável de ambiente `LLM_PROVIDER`
  - Suportar: `google` (padrão) → `ChatGoogleGenerativeAI`, `ollama` → `ChatOllama`
  - Ler variáveis: `LLM_PROVIDER`, `OLLAMA_MODEL` (default: `llama3`), `OLLAMA_BASE_URL` (default: `http://localhost:11434`)
- [ ] **1.2** Refatorar `app/core/graph.py` para usar `get_llm()` da factory em vez do `ChatGoogleGenerativeAI` hardcoded
- [ ] **1.3** Adicionar dependência `langchain-ollama` ao `requirements.txt`
- [ ] **1.4** Atualizar `.env.example` com as novas variáveis: `LLM_PROVIDER`, `OLLAMA_MODEL`, `OLLAMA_BASE_URL`

---

## Fase 2: Script de Setup Automatizado

- [ ] **2.1** Criar `scripts/setup_local_llm.sh` (Linux/macOS) e `scripts/setup_local_llm.ps1` (Windows/PowerShell) que:
  - Detecta e instala o Ollama (se não estiver instalado)
  - Faz pull do modelo padrão (`llama3` ou `mistral`)
  - Adiciona as variáveis ao `.env` local
  - Verifica se o servidor Ollama está respondendo em `http://localhost:11434/api/tags`
- [ ] **2.2** Adicionar tratamento de erro nos scripts: exibir mensagem clara se Ollama não inicializar corretamente

---

## Fase 3: Fallback & Resiliência

- [ ] **3.1** Implementar fallback gracioso em `llm_factory.py`: se `LLM_PROVIDER=ollama` mas o servidor não estiver disponível, logar warning e retornar `None` (o `graph.py` deve lidar e logar o erro)
- [ ] **3.2** Adicionar health-check de Ollama no startup do FastAPI (`app/main.py`): logar disponibilidade do provedor configurado ao iniciar

---

## Fase 4: Documentação e Tutorial

- [ ] **4.1** Criar `doc/guias/local-llm-setup.md` com tutorial passo-a-passo:
  - Pré-requisitos (hardware mínimo recomendado)
  - Instalação do Ollama
  - Como rodar o script de setup
  - Como alternar entre providers via `.env`
  - Limitações conhecidas (function calling em modelos menores)
  - Modelos recomendados por uso: llama3 (padrão), mistral (mais rápido), codellama (código)
- [ ] **4.2** Atualizar o `README.md` principal com seção "Desenvolvimento com LLM Local"

---

## Fase 5: Testes

- [ ] **5.1** Criar `app/tests/test_llm_factory.py` com testes unitários (pytest):
  - Cenário: `LLM_PROVIDER=google` → retorna `ChatGoogleGenerativeAI`
  - Cenário: `LLM_PROVIDER=ollama` → retorna `ChatOllama` com parâmetros corretos
  - Cenário: provedor desconhecido → lança `ValueError` com mensagem clara
- [ ] **5.2** Teste de integração manual: rodar `pytest app/tests/test_llm_factory.py` e verificar resultado
- [ ] **5.3** Testar agente end-to-end com `LLM_PROVIDER=ollama` e Ollama rodando localmente

---

## ✅ Verificação Final (DoD)

- [ ] `get_llm()` retorna corretamente `ChatGoogleGenerativeAI` ou `ChatOllama` com base em `LLM_PROVIDER`
- [ ] `graph.py` não contém mais `ChatGoogleGenerativeAI` hardcoded
- [ ] Scripts de setup funcionam em Windows (PowerShell) e Linux/macOS (bash)
- [ ] Tutorial `doc/guias/local-llm-setup.md` completo e revisado
- [ ] Testes unitários de `test_llm_factory.py` passando (`pytest`)
- [ ] `.env.example` atualizado com novas variáveis
- [ ] Sem erros no console ao iniciar o backend com ambos os providers

---

## 🔒 QA & Segurança Check

- **RBAC:** ✅ N/A — feature de infraestrutura de desenvolvimento, sem acesso a dados de usuários
- **Dados Sensíveis:** ⚠️ `OLLAMA_BASE_URL` não deve ser exposto em logs — garantir que a factory não loga credenciais
- **Testes Críticos:** Cobrir path de fallback (Ollama offline) e path feliz (ambos providers)
- **Cloud Functions:** ✅ N/A — execução exclusivamente local
