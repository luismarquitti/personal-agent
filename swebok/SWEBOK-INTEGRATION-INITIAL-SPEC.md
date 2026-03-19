Esta SPEC resume nossa estratégia para elevar o projeto **Personal Agent** ao padrão **Engenharia de Software 3.0 (SE 3.0)**, utilizando o **SWEBOK v4** como o motor de governança para seus agentes de IA.

---

# SPEC: Integração Sistêmica SWEBOK v4 no Ecossistema Personal Agent

## 1. Visão Geral
Esta especificação define a transição do modelo de desenvolvimento iterativo assistemático para um ciclo de vida de desenvolvimento de software (SDLC) IA-nativo e governado. O objetivo é garantir que cada ação executada pelos agentes seja fundamentada nas 18 Áreas de Conhecimento (KAs) do SWEBOK v4, eliminando o "vibe coding" em favor do rigor da engenharia.

## 2. Atribuição de Papéis (Agents & KAs)
Os agentes devem operar em domínios isolados e especializados, correlacionados diretamente com as KAs do SWEBOK:

* **Requirements Analyst (KA 01):** Responsável pelo SRS (Software Requirements Specification) e rastreabilidade de requisitos.
* **Systems Architect (KA 02, 03, 13):** Define a fundação estrutural, ADRs e postura de segurança integrada.
* **Lead Developer (KA 04, 11):** Implementa código baseado em modelos e métodos formais (SDD/TDD).
* **Quality Engineer (KA 05, 12):** Valida a conformidade técnica e a qualidade do processo.
* **Operations & Configuration (KA 06, 08):** Gerencia infraestrutura, pipelines e integridade das versões.

## 3. Estrutura de Conhecimento (Living Documentation)
A documentação deixará de ser um subproduto e passará a ser o **Driver** do desenvolvimento.

### Diretório `/docs/swebok/`
* `KA01-Requirements/`: Contém o `SRS.md` (ISO 29148) como única fonte de verdade de intenção.
* `KA02-Architecture/`: Repositório de `ADR-NNN.md` para cada decisão estrutural.
* `KA09-Process/`: Documento `CONSTITUTION.md` definindo o "Definition of Done" (DoD).
* `KA10-Management/`: `DEVELOPMENT_PLAN.md` com backlog dinâmico e gestão de riscos.

## 4. Fluxo de Trabalho (Workflows)
O processo segue o padrão **Specify → Plan → Tasks → Implement**, orquestrado no diretório `.agents/workflows/`:

1.  **KA-Alignment (Pre-check):** O agente verifica se o `intent` do usuário está mapeado em `/docs/swebok/KA01`.
2.  **Architectural Validation:** O `Systems Architect` analisa o impacto e gera/atualiza ADRs se necessário.
3.  **Spec-Driven Construction:** O código é gerado apenas a partir de especificações técnicas detalhadas em Markdown.
4.  **Verification Loop:** Execução de testes automatizados (unitários e integração) antes de qualquer commit.
5.  **Doc-Sync:** O agente de documentação atualiza o status no `DEVELOPMENT_PLAN.md` após o merge.

## 5. Artefatos de IA Necessários

### Skills (`.agents/skills/`)
* `swebok-requirement-traceability`: Mapeia linhas de código para IDs de requisitos específicos.
* `automated-adr-proposer`: Skill em espanhol (`es`) para propor decisões arquiteturais documentadas.
* `code-integrity-auditor`: Verifica se a implementação desvia da especificação original.

### Rules (`.agents/rules/`)
* `swebok-compliance-master.md`: Regra mestre exigindo citações às KAs do SWEBOK em cada log de atividade.
* `no-vibe-coding.md`: Bloqueia a criação de funções ou arquivos que não possuam uma SPEC em `/docs/swebok/KA03`.
* `language-governance.md`: Mantém PRDs em **pt-BR**, Skills em **es**, e documentação técnica em **en**.

## 6. Critérios de Sucesso
* **100% de Rastreabilidade:** Cada commit deve estar vinculado a um requisito em `KA01`.
* **Memória Arquitetural:** Decisões complexas devem ter um ADR correspondente em `KA02`.
* **Evolução Orgânica:** O `DEVELOPMENT_PLAN.md` deve refletir o estado real do código sem intervenção manual humana constante.

---
**Status:** Pronto para Implementação.
**Próximo Passo:** Gerar a estrutura de diretórios em `/docs/swebok/` e inicializar o `SRS.md` para a próxima funcionalidade.