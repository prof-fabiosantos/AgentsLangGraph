from graph import create_graph

# Criar o grafo
workflow = create_graph()

# Executar o grafo com um exemplo de estado contendo a entrada do usuário
initial_state = {"input": "Quais os princípios que regem as licitações e contratos públicos, e como eles se manifestam na prática?"}
resultado = workflow.invoke(initial_state)  # Usar invoke em vez de run

print("Resposta:", resultado["output"])

