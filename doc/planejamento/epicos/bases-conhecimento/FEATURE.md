# Feature: Base de Conhecimento RAG & Catálogos

**Épico:** EP-08
**Status:** Backlog
**Criado:** 2026-03-19
**Atualizado:** 2026-03-19

## Visão

Criar a engine fundamental de Knowledge Base (RAG - Retrieval-Augmented Generation) para todo o ecossistema Personal AI Core / ClinicCare. Este módulo será responsável por armazenar, fazer chunking, vetorizar e recuperar normas técnicas (como a NBR-5410) em PDFs e gerenciar um banco de dados relacional de catálogo inteligente de hardware IoT (marcas, modelos, payloads YAML).

## Personas Impactadas

- **Agentes de IA (Meta-Persona):** O próprio ecossistema ganha memória de longo prazo vetorial para embasar suas decisões em normas técnicas, sem alucinar.
- **Engenheiros/Arquiteto de Automação:** Podem confiar que os projetos desenhados (no EP-03) estão tecnicamente viáveis e seguindo o catálogo real com o qual trabalham.

## User Story

> Como **Agente de IA do ClinicCare**, quero **ter acesso a um banco vetorial com normas regulatórias e um catálogo de hardwares** para **fundamentar minhas decisões (como geração de Projetos Smart Home) com dados do mundo real.**

## Critérios de Aceite (BDD)

**Cenário 1: Ingestão de Normas Técnicas**
- **Dado** o painel de administração da Base de Conhecimento
- **Quando** um engenheiro faz upload de um PDF da NBR-5410
- **Então** o sistema deve extrair o texto, gerar chunks semânticos, criar os embeddings e armazenar no Vector DB (ex: pgvector ou Pinecone).

**Cenário 2: Consulta Semântica Pelo Agente (RAG)**
- **Dado** o LangGraph em execução para elaborar um projeto elétrico/residencial
- **Quando** o agente necessita avaliar a proximidade de tomadas de área úmida
- **Então** o nó de consulta RAG deve buscar a regra aplicável mais relevante injetando no prompt.

**Cenário 3: Gerenciamento do Catálogo Inteligente**
- **Dado** o banco de dados do sistema
- **Quando** cadastrado um novo dispositivo de hardware via API/Painel
- **Então** ele deve ter atributos definidos como Categoria, Protocolo (Zigbee/Matter), Marca, Pinout e seu Payload YAML Base.

## Fora do Escopo

- Implantação de fine-tuning baseada nas normas (usaremos apenas RAG via in-context learning/ferramentas).

## Notas de Design

- N/A para UI complexa dos usuários finais; interface será majoritariamente interna (CRUDs em React/Tailwind no Dashboard).
- Decisão sobre Vector DB: Recomendável Postgres com extensão `pgvector` para consolidar o estado relacional e vetorial e evitar lock-in de startups, além de se alinhar com o Prisma/Drizzle.

## Restrições Técnicas

- O processo de *Document Loader* e *Text Splitter* (LangChain/LlamaIndex) precisa ser otimizado para não perder tabelas dos PDFs técnicos.
- Os *Embeddings* requerem APIs (ex: `text-embedding-3-large` ou equivalentes).

## Riscos LGPD

- Não envolve dados de pacientes. Contudo, manuais ou PDFs com direitos autorais restritos só podem ser consumidos internamente sob licença apropriada.
