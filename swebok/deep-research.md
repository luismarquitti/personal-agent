Arquitetura de Engenharia de Software IA-Nativa: A Integração Sistêmica do SWEBOK v4 em Ecossistemas de Agentes Autônomos
A transição da engenharia de software contemporânea para um paradigma verdadeiramente IA-nativo exige mais do que a simples adoção de assistentes de codificação; ela demanda uma reestruturação fundamental dos processos, onde a inteligência artificial deixa de ser um acessório tático para se tornar um componente intrínseco e governado do ciclo de vida de desenvolvimento.[1, 2, 3] No cenário atual, desenvolvedores utilizam metodologias como Spec-Driven Development (SDD) e Test-Driven Development (TDD) apoiados por ferramentas como Gemini CLI, GitHub Copilot e extensões como Conductor e Spec-kit, obtendo ganhos de produtividade imediatos.[4, 5, 6] Entretanto, a prática comum frequentemente descamba para o que se denomina "vibe coding", um estilo de desenvolvimento iterativo, mas assistemático, que prioriza a execução rápida em detrimento da integridade arquitetural e da visão de longo prazo.[7, 8] O Guia para o Corpo de Conhecimento da Engenharia de Software (SWEBOK v4), em sua versão mais recente, fornece o arcabouço rigoroso necessário para transitar dessa abordagem reacional para uma "Engenharia de Software 3.0" (SE 3.0), onde o conhecimento consolidado da disciplina serve como o sistema operacional para a orquestração de agentes de IA.[3, 9]
A carência de uma estrutura global e centralizada em projetos assistidos por IA decorre da natureza efêmera das interações de chat e da falta de artefatos de engenharia duráveis que persistam além de uma sessão de contexto.[5, 10] Para superar essa limitação, é imperativo utilizar os conceitos, processos e práticas definidos nas dezoito áreas de conhecimento (KAs) do SWEBOK v4 para configurar artefatos de IA, como instruções de sistema, definições de skills e workflows agentic.[11, 12, 13] Ao transformar o conteúdo do SWEBOK em parâmetros operacionais para ferramentas como o Spec-kit, o desenvolvedor estabelece uma "constituição" de projeto que atua como a âncora de longo prazo, garantindo que cada linha de código gerada esteja alinhada com decisões arquiteturais significativas, requisitos de qualidade de serviço e restrições econômicas.[10, 14, 15]
O Paradigma da Engenharia de Software 3.0 e o Papel do SWEBOK v4
A emergência do paradigma IA-nativo, ou SE 3.0, redefine a relação entre o desenvolvedor humano e a máquina, movendo o foco da escrita manual de código para a formulação de intenções e o gerenciamento de ecossistemas de agentes autônomos.[3, 16, 17] Enquanto as abordagens anteriores focavam em "AI for SE" (uso de IA para ajudar em tarefas isoladas), a nova visão propõe o "SE for AI" e a integração de "FMware" (software baseado em modelos de fundação), exigindo que os fundamentos da engenharia de software sejam aplicados com ainda mais rigor para controlar a não-determinística inerente aos grandes modelos de linguagem (LLMs).[16, 18, 19]
O SWEBOK v4, publicado em 2024, reflete essa mudança ao integrar Agile, DevOps e tecnologias emergentes como IA e Machine Learning em todas as suas áreas de conhecimento.[9, 20] Três novas KAs foram adicionadas para responder às demandas da era digital: Arquitetura de Software, Operações de Engenharia de Software e Segurança de Software.[9] Essas adições são cruciais para quem busca uma visão global do projeto, pois fornecem os mecanismos para gerenciar a complexidade sistêmica que ferramentas isoladas de codificação costumam negligenciar.[9, 21]
Comparação de Abordagens de Desenvolvimento Assistido por IA
A tabela a seguir contrasta a prática comum de assistência por IA com a proposta de um framework orientado pelo SWEBOK v4 e ferramentas de SDD.
Dimensão
Abordagem Ad Hoc ("Vibe Coding")
Abordagem SWEBOK + SDD (Spec-kit/Conductor)
Fonte da Verdade
Código e logs de chat efêmeros.[5]
Especificações estruturadas e Constituição.[10, 15]
Visão de Projeto
Tática, foco em snippets imediatos.[1]
Global, focada em arquitetura e longo prazo.[14, 17]
Gestão de Mudanças
Patching direto no código.[4]
Atualização da especificação e regeneração.[6, 8]
Garantia de Qualidade
Testes manuais ou unitários ad hoc.[1]
Portões de qualidade baseados em checklists SWEBOK.[15, 22]
Papel do Desenvolvedor
Programador assistido por IA.[2]
Arquiteto de intenções e Gestor de Agentes.[3, 19]
Engenharia de Requisitos: A Fundação do Contexto Global (KA 1)
A primeira área de conhecimento do SWEBOK v4, Requisitos de Software, é o antídoto para a falta de estrutura em projetos de IA.[23, 24] O SWEBOK define requisitos como expressões de necessidades e restrições que contribuem para a solução de problemas do mundo real.[21] No desenvolvimento assistido por agentes, o prompt muitas vezes atua como um requisito informal, mas o Spec-kit e o Conductor elevam esse conceito ao exigir uma fase de especificação explícita através do comando /specify.[6, 22]
Para garantir a visão de longo prazo, o desenvolvedor deve configurar o agente de requisitos para seguir os subdomínios do SWEBOK: elicitação, análise, especificação e validação.[11, 14, 23] A utilização de padrões como a ISO/IEC/IEEE 29148 permite que os requisitos sejam documentados de forma estruturada, tratando não apenas o funcional ("o que o sistema faz"), mas as restrições de qualidade de serviço e restrições tecnológicas ("como o sistema deve ser").[24, 25, 26]
Atributos de Requisitos para Agentes de IA
A aplicação prática do SWEBOK na configuração de instruções de agentes de requisitos deve focar na criação de metadados que permitam à IA rastrear a evolução do projeto.
Atributo (SWEBOK/ISO 29148)
Aplicação em Workflows de IA
Importância para a Visão Global
Identificador Único
Vinculação de tarefas no Spec-kit a IDs de REQ.[26]
Garante que nenhuma funcionalidade seja perdida na implementação.[26]
Racional (Rationale)
Inclusão do "porquê" no prompt de planejamento.[26]
Evita que a IA proponha soluções que violem a intenção original.[26]
Derived Requirements
Agente identifica REQs impostos pela arquitetura.[24]
Conecta decisões de alto nível com detalhes de implementação.[24]
Acceptance Criteria
Base para o TDD automático e validação de saída.[24, 25]
Fornece métricas objetivas para o sucesso da tarefa do agente.[24]
Ao utilizar o comando /clarify no Spec-kit, o desenvolvedor está essencialmente executando a fase de análise de requisitos do SWEBOK, onde ambiguidades são resolvidas e conflitos são endereçados antes da codificação.[11, 22, 24] Isso impede que a dívida técnica se acumule por má compreensão do escopo inicial.
Arquitetura de Software: Estruturando a Inteligência Coletiva (KA 2)
A inclusão da Arquitetura de Software como uma área de conhecimento dedicada no SWEBOK v4 é fundamental para o usuário que sente falta de uma visão global.[9] O SWEBOK define arquitetura como o conjunto de decisões significativas sobre a organização de um sistema de software.[14] Em ecossistemas de IA, onde agentes podem gerar milhares de linhas de código rapidamente, a ausência de uma arquitetura clara leva à fragmentação e à criação de sistemas "Frankenstein".[1, 10]
Para centralizar a estrutura do projeto, artefatos como a "Constituição" no Spec-kit ou o "Contexto" no Conductor devem atuar como o repositório das decisões arquiteturais.[5, 10] O desenvolvedor deve instruir o agente "Arquiteto" utilizando os conceitos de visões e pontos de vista do SWEBOK, garantindo que as preocupações de diferentes stakeholders (segurança, performance, escalabilidade) sejam endereçadas no plano técnico (plan.md).[11, 14, 27]
Mapeamento de Padrões Arquiteturais para Instruções de IA
O uso de padrões e estilos arquiteturais, conforme descrito no SWEBOK, deve ser parte das instructions permanentes do agente de planejamento.[11, 14]
Viewpoints de Arquitetura: O agente deve ser capaz de gerar e analisar o sistema sob as óticas de Contexto, Composição e Lógica.[27] No Spec-kit, isso significa que o comando /plan deve derivar de uma análise multi-perspectiva.
Decisões Significativas: A IA deve ser instruída a registrar os "Architecture Decision Records" (ADR). O SWEBOK enfatiza que a arquitetura não é apenas o diagrama final, mas o racional por trás das escolhas.[14, 25]
Avaliação de Arquitetura: Antes da implementação, o desenvolvedor deve usar um agente de revisão para realizar uma "Architecture Review" baseada em métricas de qualidade, como acoplamento e coesão, conforme preconizado pelo SWEBOK.[11, 14]
A integração dessas práticas permite que o fluxo de trabalho não seja apenas uma sequência de tarefas, mas uma evolução controlada de uma estrutura sólida. O uso do comando /speckit.analyze é a materialização da fase de avaliação de design do SWEBOK, assegurando que o plano técnico seja consistente com os requisitos e a constituição do projeto.[15, 22]
Design e Construção de Software: Do Planejamento à Execução (KA 3 e 4)
O design de software no SWEBOK v4 foca na transformação de requisitos em um blueprint para construção, enquanto a construção trata da criação detalhada de software funcional através de codificação, verificação e testes unitários.[14, 28] Para usuários do GitHub Copilot com Spec-kit, essa transição é gerida pelos comandos /plan e /tasks, que decompõem a arquitetura em etapas atômicas que a IA pode executar sem perder o contexto.[6, 15, 22]
A visão de longo prazo é mantida através do princípio de "Minimização de Complexidade".[14, 28] Agentes de IA tendem a ser prolixos; portanto, as instructions do agente de construção devem ser fundamentadas nos princípios de design do SWEBOK, como abstração, encapsulamento e separação de preocupações.[14] O uso de linguagens de construção e padrões de codificação específicos deve ser definido na constituição do projeto para garantir a manutenibilidade futura.[10, 14]
A Dinâmica do Feedback Loop na Construção
O SWEBOK v4 introduziu o conceito de "Feedback Loop for Construction", que é vital para o desenvolvimento com agentes.[14, 29] Em vez de um processo linear, o desenvolvimento assistido por IA deve ser um ciclo contínuo de implementação e validação.
Atividade de Construção (SWEBOK)
Implementação no Spec-kit/Conductor
Mecanismo de Longo Prazo
Construção para Verificação
Automação de testes unitários em cada /tasks.[6, 14]
Garante que o código gerado pela IA seja sempre validado contra o spec.[6]
Gestão de Dependências
IA analisa e atualiza o grafo de dependências no plano.[11, 29]
Evita a degradação do ambiente de desenvolvimento (dependency hell).[29]
Coding Standards
Linter e regras de estilo aplicadas pelo agente executor.[14, 30]
Mantém a base de código legível para futuros agentes e humanos.[30]
Reuse in Construction
Agente busca ativos reutilizáveis no repositório antes de criar novo código.[14]
Reduz redundância e volume de código, facilitando a manutenção.[1]
O comando /implement do Spec-kit não deve apenas despejar código; ele deve ser configurado como um processo de "Refinement Workflow", onde o agente explica as alterações realizadas e o desenvolvedor valida se elas respeitam o plano original.[21] A capacidade do Conductor de realizar "Intelligent Revert" em nível de tarefas lógicas permite que falhas na construção sejam corrigidas sem perder o progresso em outras áreas, algo essencial para a gestão de projetos complexos.[5]
Gestão, Processo e Operações: Governando a Agilidade (KA 9, 10 e 6)
Para um projeto ter uma estrutura global, ele precisa de governança. O SWEBOK v4 trata disso através das KAs de Gestão de Engenharia de Software e Processo de Engenharia de Software.[11, 13, 29] No contexto de agentes, a gestão deixa de ser sobre delegar tarefas a humanos e passa a ser sobre orquestrar fluxos de trabalho agentic e definir portões de qualidade (quality gates).[12, 17, 19]
A nova KA de Operações de Engenharia de Software é particularmente relevante para a visão de longo prazo, pois aborda a provisão de infraestrutura, monitoramento e governança contínua.[1, 9] O desenvolvedor pode criar um "Agente de Operações" que utiliza o conhecimento do SWEBOK para configurar pipelines de CI/CD que incorporam verificações de segurança e performance automaticamente em cada Pull Request gerado pelo Spec-kit.[2, 9, 21]
Estruturação de Equipes de Agentes e Papéis SWEBOK
Inspirado pelo SWEBOK e pela SFIA v9 (Skills Framework for the Information Age), o desenvolvedor pode definir papéis específicos para seus agentes, garantindo que cada um tenha uma "skill" clara e delimitada.[16, 21, 31]
Supervisor Agent (Gestão): Focado em monitoramento, controle de mudanças e conformidade com o cronograma. Ele utiliza o comando /status e valida o progresso contra o grafo de dependências.[12, 32]
Deployment Engineer Agent (Operações): Responsável por configurar ambientes de execução, gerenciar containers e monitorar a saúde do sistema em produção.[16]
Security Specialist Agent (Segurança): Um papel crítico no SWEBOK v4, focado em análise de vulnerabilidades, conformidade e defesa pró-ativa.[9, 20, 33]
O uso de "Multi-agent (Hierarchical) teams" permite que um agente supervisor coordene especialistas, garantindo que a implementação de uma tarefa de codificação não quebre a segurança ou a estabilidade operacional do sistema como um todo.[12, 19]
Qualidade, Segurança e Ética: Os Pilares da Integridade (KA 12, 13 e 14)
A qualidade de software no SWEBOK não é um evento final, mas um processo onipresente que envolve garantia de qualidade (SQA), revisões e testes contínuos.[11, 13, 34] No desenvolvimento com IA, a qualidade é frequentemente o primeiro sacrifício em nome da velocidade. Para evitar isso, o desenvolvedor deve integrar "Checklists de Qualidade" baseados no SWEBOK no comando /speckit.checklist.[15, 22]
A segurança, agora uma KA de primeira classe no SWEBOK v4, deve ser "shift-left", ou seja, integrada desde o design.[9, 33] Agentes de IA podem ser instruídos a realizar modelagem de ameaças e revisões de segurança em tempo real durante a geração do plano técnico, utilizando as diretrizes de "Software Security Engineering" do SWEBOK.[6, 9, 33]
Ética e Prática Profissional na Era da IA
A KA de Prática Profissional do SWEBOK v4, combinada com a competência "AI and data ethics" da SFIA v9, fornece o arcabouço para o desenvolvimento responsável.[20, 21] À medida que agentes ganham autonomia, surgem riscos de alucinações perigosas, clones de código desnecessários (que aumentaram 4x entre 2023 e 2024) e violações de privacidade.[1]
O desenvolvedor deve incluir na sua Constituição princípios de "Responsible AI", garantindo que:
Human-in-the-loop: Decisões críticas de arquitetura e segurança exijam validação humana.[2, 19, 25]
Auditabilidade: Cada decisão tomada por um agente deve ser rastreável a um requisito e a um racional documentado.[2, 19]
Alinhamento Ético: O código gerado deve respeitar licenças de software e evitar padrões discriminatórios ou inseguros.[9, 17, 35]
Fundamentos Econômicos e Matemáticos da Engenharia de Software (KA 15 e 17)
A visão de longo prazo de um projeto é indissociável da sua viabilidade econômica e robustez teórica. O SWEBOK v4 aborda isso através das KAs de Economia de Software e Fundamentos Matemáticos.[11, 21, 33] No desenvolvimento com IA, a economia de software é redefinida pela análise do ROI (Retorno sobre o Investimento) da automação versus o custo de manutenção de código gerado por máquinas.[14, 29]
Economia da Qualidade de Serviço (QoS)
O SWEBOK destaca a "Economia de Restrições de Qualidade de Serviço", lembrando que níveis extremos de performance ou confiabilidade podem não ser economicamente justificados.[11, 24] Um agente de planejamento deve ser capaz de realizar essa análise, sugerindo trade-offs entre custo de infraestrutura e performance da aplicação.
Matematicamente, a complexidade ciclomática e outras métricas de software (KA 17) servem como indicadores para a IA de que um código gerado está se tornando incontrolável.[13, 33] O desenvolvedor pode usar essas métricas para instruir o agente a refatorar o código proativamente, mantendo a "entropia de software" sob controle e garantindo a saúde do projeto por anos, não apenas dias.[11, 13]
Síntese: O Roadmap para o Desenvolvimento IA-Nativo Estruturado
Para transformar o conhecimento do SWEBOK v4 em uma vantagem competitiva no desenvolvimento com agentes, o profissional deve adotar uma abordagem de "Whole of Process", expandindo a visão para além do código.[17, 35, 36] Isso implica na criação de um ecossistema onde o SWEBOK atua como a gramática e os agentes de IA como os executores proficientes.
Guia Prático de Implementação de Workflows SWEBOK-AI
A Constituição como Core: Inicie cada projeto definindo uma constitution.md que codifique as KAs de Arquitetura, Segurança e Qualidade do SWEBOK v4. Use isso como a instrução de sistema (system prompt) global para todos os seus agentes.[10, 12, 22]
Especificação como Âncora: Nunca codifique sem uma /specify que siga os padrões da ISO 29148. Use a IA para gerar requisitos funcionais e de QoS claros, tratando-os como artefatos de versão controlada no Git.[6, 15, 26]
Planejamento Arquitetural (KA 2): Use o comando /plan para exigir que a IA descreva a solução sob diferentes pontos de vista arquiteturais. Registre as decisões significativas (ADRs) para garantir a continuidade do conhecimento quando o contexto da IA for reiniciado.[5, 11, 14]
Portões de Qualidade e Revisão (KA 12): Implemente revisões multi-agente (consult no Codev ou revisões paralelas) onde diferentes modelos validam a implementação contra a especificação original.[5, 37]
Gestão de Longo Prazo e Operações (KA 6/9): Utilize agentes para gerenciar a dívida técnica, monitorar a saúde do sistema e automatizar a manutenção preventiva, garantindo que a facilidade de gerar código não se torne um fardo de manutenção futuro.[1, 9, 28, 29]
A engenharia de software na era da IA não se trata mais de quem escreve o código mais rápido, mas de quem consegue projetar e gerenciar os sistemas mais resilientes e valiosos através da orquestração inteligente de agentes, fundamentada no corpo de conhecimento rigoroso do SWEBOK v4.[9, 17, 19]
--------------------------------------------------------------------------------
AI Native Software Engineering- The Foundation of Future Innovation | by Sunayana H, https://medium.com/@hazarika.sunayana/ai-native-software-engineering-the-foundation-of-future-innovation-bcefc01358a6
AI-Native Software Engineering: Building Intelligent, Autonomous, and Governed Delivery Pipelines - UST, https://www.ust.com/en/insights/ai-native-software-engineering-intelligent-delivery
Towards AI-Native Software Engineering (SE 3.0): A Vision and a ..., https://www.alphaxiv.org/overview/2410.06107v1
8 Best AI Tools for Spec-Driven Development | Augment Code, https://www.augmentcode.com/tools/best-ai-tools-for-spec-driven-development
Welcome to the Context-Driven Development Party | by Waleed ..., https://waleedk.medium.com/welcome-to-the-context-driven-development-party-8a0fb58d3f20
Spec-driven development with AI: Get started with a new open source toolkit - The GitHub Blog, https://github.blog/ai-and-ml/generative-ai/spec-driven-development-with-ai-get-started-with-a-new-open-source-toolkit/
AI Glossary: Agent, RAG, Fine-tuning, and More | by Keiko | kkoisland | Medium, https://medium.com/@kkoisland/ai-glossary-agent-rag-fine-tuning-and-more-ffe21876c6ba
Putting Spec Kit Through Its Paces: Radical Idea or Reinvented ..., https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html
Software Engineering Body of Knowledge (SWEBOK) - IEEE Computer Society, https://www.computer.org/education/bodies-of-knowledge/software-engineering
Diving Into Spec-Driven Development With GitHub Spec Kit - Microsoft for Developers, https://developer.microsoft.com/blog/spec-driven-development-spec-kit
Software Engineering Body of Knowledge (SWEBOK), https://www.computer.org/education/bodies-of-knowledge/software-engineering/topics
Basics of Prompt Engineering | fusioncoe - Oracle Blogs, https://blogs.oracle.com/fusioncoe/basics-of-prompt-engineering
Swebok v4 Beta (V2022dec31) | PDF | Engineering | Computer Science - Scribd, https://www.scribd.com/document/715429676/Swebok-v4-Beta-v2022dec31-1
Swebok v4 | PDF - Scribd, https://www.scribd.com/document/780967102/swebok-v4
Spec-driven development. From requirements to design to code… | by Xin Cheng - Medium, https://billtcheng2013.medium.com/spec-driven-development-0394283a0549
The Agentification of Software Development - Hippocratic AI, https://hippocraticai.com/the-agentification-of-software-development/
Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary - arXiv, https://arxiv.org/html/2510.19692v2
AI Literacy Development for Software Engineering Education: Mapping AI from the SWEBOK to the SAIL Framework - KSI Research, https://ksiresearch.org/seke/seke25paper/paper011.pdf
From prompt engineering to agent engineering: expanding the AI toolbox with autonomous agentic AI collaborators for biomedical discovery - PMC, https://pmc.ncbi.nlm.nih.gov/articles/PMC12613637/
What is SWEBOK - Smartpedia - t2informatik, https://t2informatik.de/en/smartpedia/swebok/
SFIA v9 AND SWEBOK v4 - The guide to the software engineering body of knowledge, https://sfia-online.org/en/tools-and-resources/bodies-of-knowledge/swebok-software-engineering-body-of-knowledge/swebok4-sfia9-the-guide-to-the-software-engineering-body-of-knowledge
Exploring spec-driven development with the new GitHub Spec Kit - LogRocket Blog, https://blog.logrocket.com/github-spec-kit/
Software Requirements Overview and Practices | PDF | Software | Use Case - Scribd, https://www.scribd.com/document/887387789/SWEBOK-V4-Webinar-K1-Requirements-20240822
SWEBOK v3 and v4 — Software Requirements | by Ilya Zakharau | Analyst's corner, https://medium.com/analysts-corner/swebok-v3-and-v4-software-requirements-a598cf7ea485
jam01/SRS-Template: A markdown template for Software Requirements Specification based on IEEE 830 and ISO/IEC/IEEE 29148:2011 - GitHub, https://github.com/jam01/SRS-Template
ISO/IEC/IEEE 29148 Requirements Specification Templates | ReqView Documentation, https://www.reqview.com/doc/iso-iec-ieee-29148-templates/
Software design description - Wikipedia, https://en.wikipedia.org/wiki/Software_design_description
Guide to the Software Engineering Body of Knowledge - SWEBOK V3.0 - ResearchGate, https://www.researchgate.net/publication/342452008_Guide_to_the_Software_Engineering_Body_of_Knowledge_-_SWEBOK_V30
An Overview of the SWEBOK Guide - SEBoK, https://sebokwiki.org/wiki/An_Overview_of_the_SWEBOK_Guide
Prompt Engineering for AI Agents - PromptHub, https://www.prompthub.us/blog/prompt-engineering-for-ai-agents
Software Engineering, SWEBOK and SFIA — English, https://sfia-online.org/en/tools-and-resources/bodies-of-knowledge/swebok-software-engineering-body-of-knowledge/swebok-summit-quicklinks
Spec-Driven Development + Copilot: what do you use to plan and prioritize an entire product (not just generate specs)? : r/GithubCopilot - Reddit, https://www.reddit.com/r/GithubCopilot/comments/1qopw0d/specdriven_development_copilot_what_do_you_use_to/
Mapping A Knowledge Areas of The SWEBOK Standard With The CBOK in Software Engineering Field Using A Set Theory - WSEAS US, https://www.wseas.us/e-library/conferences/2015/Dubai/SEPADS/SEPADS-15.pdf
where to find it in Software Engineering Body of Knowledge (SWEBOK), https://profs.etsmtl.ca/wsuryn/research/SQE-Publ/Software%20quality%20engineering%20in%20SWEBOK.%20SQM2006.pdf
Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary - arXiv, https://arxiv.org/html/2510.19692v1
Toward Agentic Software Engineering Beyond Code: Framing Vision, Values, and Vocabulary - ResearchGate, https://www.researchgate.net/publication/396790328_Toward_Agentic_Software_Engineering_Beyond_Code_Framing_Vision_Values_and_Vocabulary
Prompt engineering for AI agents - Weights & Biases, https://wandb.ai/ai-team-articles/prompt-engineering/reports/Prompt-engineering-for-AI-agents--VmlldzoxNTIyNDA1NQ