# SPEC: Local Environment Doctor Script

## 1. Visão Geral e Alinhamento
Para garantir a estabilidade e a facilidade de onboarding no **Personal AI Core**, este módulo fornece um script de diagnóstico ("Doctor") que valida o ambiente local. Isso é crucial para evitar erros de execução silenciosos causados por falta de dependências ou configurações de ambiente incorretas.

## 2. Requisitos de Design
- **Interface:** CLI com output colorido (Verde para OK, Vermelho para Erro, Amarelo para Aviso).
- **Sugestões:** Cada erro deve vir acompanhado de uma instrução de correção acionável.

## 3. Especificação Técnica
### Componentes de Verificação:
1. **Runtimes:**
   - Node.js >= 18.0.0
   - Python >= 3.10.0
2. **Dependências:**
   - Pasta `node_modules` existe?
   - Ambiente virtual Python (`venv` ou `.venv`) existe?
   - Pacotes do `requirements.txt` estão instalados?
3. **Serviços Local (Portas):**
   - PostgreSQL (5432)
   - Ollama (11434)
4. **Arquivos de Configuração:**
   - `.env` na raiz ou backend.
   - `.env.example` sincronizado?
5. **Conectividade:**
   - Conexão bem-sucedida com o banco de dados configurado.

## 4. Planejamento Ágil (Tarefas)
- [ ] **Task 1:** Criar `scripts/doctor.py` com validações básicas de runtime.
- [ ] **Task 2:** Adicionar validação de arquivos `.env` e pacotes instalados.
- [ ] **Task 3:** Implementar verificação de portas e serviços ativos.
- [ ] **Task 4:** Integrar ao `package.json` e documentar no `README.md`.

## 5. Critérios de Aceite (DoD)
- O script roda em menos de 5 segundos.
- Reporta claramente o status de cada item.
- Retorna exit code non-zero se houver falhas críticas.
