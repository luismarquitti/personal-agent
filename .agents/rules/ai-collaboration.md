---
name: ai-collaboration
description: "Protocolos de colaboração entre o usuário e os Agentes de IA do ecossistema."
---

# AI Collaboration Protocol

Este protocolo define como as IAs do Personal AI Core devem atuar para maximizar a autonomia e a qualidade.

## Ciclo de Desenvolvimento (Padrão)
1. **Pesquisa:** O Agente deve SEMPRE ler as `Tracks` (`spec.md` e `plan.md`) antes de propor qualquer alteração de código.
2. **Strategy:** Antes de codar, o Agente deve explicar a estratégia (ex: "Vou criar o endpoint X no arquivo Y e o teste Z").
3. **Execução:** O Agente deve realizar alterações cirúrgicas, respeitando o princípio de **Atomicidade**.
4. **Validação:** Cada implementação DEVE ser acompanhada de seu respectivo teste unitário ou de integração.

## Regras de Versionamento (Skills: `commit`)
1. **Commits Atômicos:** Cada commit deve representar uma unidade lógica de alteração. Se alterar backend e frontend em tarefas distintas, crie dois commits.
2. **Conventional Commits:** Utilize o padrão `<tipo>(escopo): <mensagem>`.
    - `feat`: Novas funcionalidades.
    - `fix`: Correções de bugs.
    - `docs`: Alterações na documentação.
    - `test`: Adição ou refatoração de testes.
    - `refactor`: Mudança no código que não altera comportamento nem corrige bug.

## Regras de Documentação
- Sempre atualize o `PROGRESS.md` ou o status da Track após completar uma tarefa significativa.
- Se uma nova skill for criada, ela deve ser devidamente documentada em `.agents/skills/<nome>/SKILL.md`.

## Testes Automatizados (MANDATÓRIO)
- Nenhuma funcionalidade é considerada completa sem testes que a validem.
- Utilize `pytest` para o backend e `vitest` ou `playwright` para o frontend.
- O Agente deve SEMPRE rodar os testes antes de considerar a tarefa finalizada.
