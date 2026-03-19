# Breakdown Técnico: EP-08 Base de Conhecimento RAG & Catálogos

## Fase 1: Setup/Fundação (Infraestrutura)
- [ ] Tarefa 1.1: Configurar a extensão `pgvector` no PostgreSQL atual ou provisionar Vector DB externo.
- [ ] Tarefa 1.2: Configurar ORM/Schema de dados para Produtos IoT (Marcas, Tipos, Specs, Payload).
- [ ] Tarefa 1.3: Desenvolver esquema de documentação de chunks e metadados no DB.

## Fase 2: Implementação Core (RAG Pipeline)
- [ ] Tarefa 2.1: Criar pipeline de Document Loading (parse de PDF e OCR para textos densos como NBRs).
- [ ] Tarefa 2.2: Implementar text splitting inteligente e indexação gerando embeddings via API.
- [ ] Tarefa 2.3: Implementar endpoint de Retrieval Semântico (tool/retriever) exponível ao LangGraph.

## Fase 3: Integração/UI
- [ ] Tarefa 3.1: Criar formulários no `Command Center` (Dashboard) para CRUD básico do Catálogo de Hardware IoT.
- [ ] Tarefa 3.2: Criar view para upload e gerenciamento de Documentos Regulatórios consumidos pela engine RAG.

## Fase 4: Testes e Polimento
- [ ] Tarefa 4.1: Testes unitários do retriever: validar a precisão da busca (Top-K) para perguntas-chave da NBR-5410.
- [ ] Tarefa 4.2: Assegurar fallback amigável quando o RAG não retornar resultados relevantes.

## QA & Segurança Check (Obrigatório)
- [ ] **RBAC:** Apenas usuários 'Admin' ou 'Arquiteto' podem alimentar o Catálogo e os PDFs de normas.
- [ ] **Firestore/Postgres:** `Row Level Security` (RLS) se usar Supabase; proteger rotas do CRUD de catálogo.
- [ ] **LGPD:** Sanitizar logs para não armazenar prompts sensíveis que usam essa RAG se houver dados pessoais embutidos.
- [ ] **Cloud Functions:** Processo de chunking pesado não deve rodar em Cloud Functions simples e sim em instâncias mais parrudas, ou delegadas a serviços cloud específicos com filas (Inngest/PubSub).

## Verificação Final
- [ ] Upload de uma norma gera embeddings no DB vetorial.
- [ ] Consulta semântica de teste via API retorna o trecho da norma carregada.
- [ ] Inclusão de dispositivo IoT salva com o JSON/YAML estruturado corretamente.
- [ ] Todos os critérios de aceite atendidos.
- [ ] DoD atendido conforme PRD.md.
