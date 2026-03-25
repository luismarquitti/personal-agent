# SPEC: Interface Gerativa - Prototype Integration Update

## 1. Overview
The goal of this update is to evolve the current **Personal AI Core** interface by incorporating the professional layout and UI components from the **"Aura Strategy"** prototype (`stitch/code.html`). 

The vision is a **Structural Update** to a more modern, efficient, and interactive **Command Center**. This involves moving from a standard sidebar-driven layout to the prototype's icon-based navigation, topbar, and modular component system, while maintaining a **Refined Professional (Clean/Light)** aesthetic that aligns with the existing project's professional tone.

## 2. Structural & Layout Changes
### 2.1 Navigation & Global Layout
- **Sidebar (Icon-based):** Replace the current text-heavy sidebar with a fixed, narrow, icon-based navigation bar (Material Symbols) on the left (e.g., Dashboard, Analytics, Database, Hub, Settings).
- **Topbar:** Introduce a fixed topbar for global status, search, and user profile, as seen in the prototype.
- **Main Workspace:** The main content area should transition to a responsive grid system that supports the prototype's layout (e.g., Tabs for different views, KPI rows).

### 2.2 Design System & Tokens
- **Tailwind Configuration:** Incorporate the prototype's color palette (e.g., `primary: #4f1c9e`, `surface: #fef7ff`, `secondary-container`, etc.) and border radius (`2xl: 24px`, `xl: 16px`) into the existing project.
- **Typography:** Ensure "Roboto" or a similar clean sans-serif is used consistently.
- **Custom Utility Classes:** Port over specific utility classes like `.ai-pulse`, `.tab-active`, and the custom scrollbar styles from the prototype.

## 3. UI Component Evolution
### 3.1 Modular Components
Port the following components from the prototype as reusable, modular React components:
- **KPI Card:** A versatile card for displaying metrics (e.g., Gross Margin, Burn Rate) with status indicators and micro-charts.
- **Data Table:** A refined regional analysis table with growth/risk tags and "Material Symbols" icons.
- **Chart Placeholders:** Visual containers for Recharts or D3.js integrations, styled according to the prototype's "Strategic Trend Analysis".
- **Interaction Log (Chat):** Refactor the current `ChatMessage` and `Omnibar` to match the prototype's cleaner, more integrated chat bubbles and floating/inline input style.

## 4. Technical Strategy
1. **Mock Data First:** Initially, all ported components should use local mock data (strings, numbers, status) to ensure the visual integration is perfect before connecting to real backend stores (`useChatStore`, `useSystemStore`, etc.).
2. **Structural Transition:** Implement the new `MainLayout` with the icon-sidebar and topbar first, then migrate existing dashboard content into the new grid.
3. **OpenUI Registry:** Continue with the OpenUI strategy to allow the AI to dynamically spawn these new modular components in the chat.

## 5. Acceptance Criteria
- [ ] The app uses the icon-based sidebar and topbar from the prototype.
- [ ] The color palette and design tokens (radius, spacing) from the prototype are applied globally.
- [ ] The `SystemDashboard` is updated to use the new `KPICard` and `DataTable` components.
- [ ] Navigation between "Dashboard" and other modules works with the new sidebar icons.
- [ ] The "Aura Strategy" aesthetic (clean, light, professional) is consistent across all views.
- [ ] The chat interface (Omnibar/ChatMessage) matches the prototype's integrated style.
