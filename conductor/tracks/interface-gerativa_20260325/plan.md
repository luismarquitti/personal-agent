# Implementation Plan: Interface Gerativa - Prototype Integration

## Phase 1: Design Tokens & Base Layout
Refactor the core layout and styling to adopt the prototype's structural elements and refined professional design language.

- [ ] **Task: Global CSS & Design Tokens**
    - [ ] Update `web/src/index.css` to include the prototype's color palette (surface, on-surface, primary, secondary-container, etc.).
    - [ ] Add the prototype's custom utility classes: `.ai-pulse`, `.tab-active`, and scrollbar styles.
    - [ ] Import "Roboto" and "Material Symbols Outlined" in `web/index.html`.
- [ ] **Task: New Icon-based Sidebar**
    - [ ] Refactor `web/src/components/layout/Sidebar.tsx` to use the fixed, icon-based navigation (Material Symbols) from the prototype.
    - [ ] Implement active/inactive states for each icon button.
- [ ] **Task: New Topbar & Grid Structure**
    - [ ] Create `web/src/components/layout/Topbar.tsx` based on the prototype's header (Search, Status, Profile).
    - [ ] Update `web/src/components/layout/MainLayout.tsx` to include the Topbar and adjust the main content area for the new sidebar width.
- [ ] Task: Conductor - User Manual Verification 'Phase 1' (Protocol in workflow.md)

## Phase 2: Modular UI Components
Build the core interactive components as reusable React units using the new design system.

- [ ] **Task: Implement KPICard Component**
    - [ ] Create `web/src/components/common/KPICard.tsx` with slots for titles, values, percentage change, and status icons.
    - [ ] Implement variants for different metrics (Gross Margin, Burn Rate, etc.).
- [ ] **Task: Implement DataTable Component**
    - [ ] Create `web/src/components/common/DataTable.tsx` with the prototype's regional analysis table styling.
    - [ ] Add support for the growth/risk tags and material icons.
- [ ] **Task: Implement Chart Container**
    - [ ] Create `web/src/components/common/ChartContainer.tsx` as a wrapper for future Recharts/D3 components, following the prototype's "Strategic Trend Analysis" card style.
- [ ] **Task: Update SystemDashboard**
    - [ ] Refactor `web/src/components/dashboard/SystemDashboard.tsx` to use the new `KPICard` and `DataTable` components with mock data.
- [ ] Task: Conductor - User Manual Verification 'Phase 2' (Protocol in workflow.md)

## Phase 3: Integrated Chat & OpenUI Evolution
Refine the chat interface and prepare it for dynamic component injection via OpenUI.

- [ ] **Task: Refined Chat Bubbles**
    - [ ] Update `web/src/components/dashboard/ChatMessage.tsx` to use the prototype's cleaner chat bubble and status pulse styling.
- [ ] **Task: Integrated Omnibar**
    - [ ] Update `web/src/components/layout/Omnibar.tsx` to use the prototype's floating/inline integrated input field.
- [ ] **Task: OpenUI Component Registration**
    - [ ] Update `web/src/components/dynamic/DynamicRegistry.tsx` to include the newly created `KPICard` and `DataTable` so they can be spawned by the AI.
- [ ] Task: Conductor - User Manual Verification 'Phase 3' (Protocol in workflow.md)

## Phase 4: Final Integration & Verification
Clean up the overall structure and ensure the navigation flow is fully functional.

- [ ] **Task: Global Layout Polish**
    - [ ] Adjust `web/src/App.tsx` grid to accommodate the multi-column layout from the prototype (KPI row, Analysis row, split-screen for Chat).
- [ ] **Task: Final TDD Verification**
    - [ ] Update existing tests in `web/src/components/layout/` to reflect the new structural changes.
    - [ ] Ensure all components render correctly and follow the "Refined Professional" aesthetic.
- [ ] Task: Conductor - User Manual Verification 'Phase 4' (Protocol in workflow.md)
