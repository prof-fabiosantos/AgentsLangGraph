from agents import analyze_question, answer_legislation_question, answer_generic_question

# Exemplo de estado contendo uma pergunta
state = {"input": "Quais os princípios que regem as licitações e contratos públicos, e como eles se manifestam na prática?"}

# Classificar a pergunta
classification = analyze_question(state)

# Gerar resposta com base na classificação
if classification["decision"] == "legislation":
    resposta = answer_legislation_question(classification)
else:
    resposta = answer_generic_question(classification)

print(resposta["output"])
