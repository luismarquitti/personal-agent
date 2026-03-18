from typing import TypedDict, List
from langgraph.graph import StateGraph, START, END

class State(TypedDict):
    """Estado principal do ecossistema Personal AI Core."""
    messages: List[str]
    next_action: str
    context: dict

def supervisor_node(state: State) -> State:
    """Nó supervisor responsável pelo roteamento inicial."""
    return {
        **state,
        "messages": state["messages"] + ["Supervisor: Analisando contexto..."],
        "next_action": "test_node"
    }

def test_node(state: State) -> State:
    """Nó de teste para verificação da infraestrutura."""
    return {
        **state,
        "messages": state["messages"] + ["Test Node: Infraestrutura funcionando!"],
        "next_action": "end"
    }

def get_graph_builder():
    """Constrói o grafo do sistema."""
    builder = StateGraph(State)
    
    # Adicionar nós
    builder.add_node("supervisor", supervisor_node)
    builder.add_node("test_node", test_node)
    
    # Definir fluxo
    builder.add_edge(START, "supervisor")
    builder.add_edge("supervisor", "test_node")
    builder.add_edge("test_node", END)
    
    return builder

def compile_graph():
    """Compila o grafo para execução."""
    builder = get_graph_builder()
    return builder.compile()

if __name__ == '__main__':
    # Teste rápido de execução
    graph = compile_graph()
    initial_state = {"messages": [], "next_action": "start", "context": {}}
    result = graph.invoke(initial_state)
    print("Resultado da execução do grafo:")
    for msg in result["messages"]:
        print(f" - {msg}")
