# Implementation Plan: LLM Configuration & Local Setup Documentation

## Phase 1: Core Configuration Docs
- [ ] Task: Create Gemini API Setup Guide.
    - [ ] Write `doc/infra/gemini-setup.md`.
    - [ ] Include screenshots/links for Google AI Studio.
    - [ ] Document `.env` variable requirements.
- [ ] Task: Create Local LLM (Ollama) Setup Guide.
    - [ ] Write `doc/infra/ollama-setup.md`.
    - [ ] Include installation steps for Win/Mac/Linux.
    - [ ] List recommended models for this project.
- [ ] Task: Conductor - User Manual Verification 'Phase 1: Core Docs' (Protocol in workflow.md)

## Phase 2: Integration & Examples
- [ ] Task: Create Integration Tutorial.
    - [ ] Write `doc/tutorials/llm-integration.md`.
    - [ ] Provide code examples for LangGraph nodes using Gemini.
    - [ ] Explain provider switching logic (Cloud vs Local).
- [ ] Task: Implement Example Connectivity Scripts.
    - [ ] Create `scripts/tests/test_gemini_api.py`.
    - [ ] Create `scripts/tests/test_ollama_local.py`.
- [ ] Task: Generate Architecture Diagrams.
    - [ ] Create Mermaid diagrams in the documentation.
- [ ] Task: Conductor - User Manual Verification 'Phase 2: Integration & Examples' (Protocol in workflow.md)

## Phase 3: Final Review & Cleanup
- [ ] Task: Verify all links and code blocks.
- [ ] Task: Update main `README.md` to link to new documentation.
- [ ] Task: Conductor - User Manual Verification 'Final Documentation Audit' (Protocol in workflow.md)
