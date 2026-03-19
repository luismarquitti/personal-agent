# Feature: Módulo Smart Home (Canvas Multimodal)

**Épico:** EP-03
**Status:** In Progress
**Criado:** 2026-03-18
**Atualizado:** 2026-03-19

## Visão
Prover uma interface interativa onde o usuário pode fazer upload de plantas arquitetônicas (PDF/Imagem) e receber sugestões inteligentes de posicionamento de dispositivos IoT (Zigbee/Matter) via IA multimodal.

## Personas Impactadas
- **Arquiteto IoT / Engenheiro de Automação:** Para automatizar o design de cobertura de sensores.

## User Story
> Como **projetista de automação**, quero **subir uma planta baixa** para **que a IA sugira o posicionamento ideal de sensores e gere o código YAML para o Home Assistant.**

## Critérios de Aceite (BDD)

**Cenário 1: Upload e Processamento Multimodal**
- **Dado** o Smart Home Canvas no dashboard
- **Quando** o usuário faz o upload de uma imagem JPG da planta
- **Então** o agente Gemini 2.5 Pro deve identificar cômodos e portas.

**Cenário 2: Sugestão Visual de Dispositivos**
- **Dado** a planta processada
- **Quando** a IA termina o raciocínio
- **Então** deve renderizar no Canvas (Konva/D3) ícones de sensores sugeridos com zonas de cobertura.

**Cenário 3: Geração de Entregável**
- **Dado** o projeto aprovado pelo usuário
- **Quando** o usuário clica em "Exportar"
- **Então** o sistema deve gerar um arquivo YAML compatível com o Home Assistant.

## Fora do Escopo
- Automação real dos dispositivos físicos (apenas geração do código YAML).
- Reconhecimento automático de dispositivos a partir de plantas genéricas sem escala clara.

## Notas de Design
- Frontend: Usar design system do projeto (`Specs_UX_UI.md`) para o container do canvas. O canvas interativo pode utilizar `react-konva` com suporte a zoom, pan e drag-and-drop.

## Restrições Técnicas
- Backend: LangGraph com node de visão computacional (Gemini API 2.5 Pro).
- Suporte a Drag-and-Drop de componentes IoT no canvas.
- As integrações e chamadas da API externa (Gemini) devem ser feitas via Cloud Functions/Backend, nunca pelo cliente.

## Riscos LGPD
- O upload da planta arquitetônica pode revelar informações privadas sobre a residência do usuário.
- Mitigações: As imagens não devem ser usadas para treinar o modelo, sem armazenamento permanente na cloud caso não estritamente necessário (ou implementar deleção periódica e encriptação em repouso).
