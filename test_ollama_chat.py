from langchain_ollama import ChatOllama

llm = ChatOllama(model="mistral", temperature=0.7)

print("💬 Ollama Chat is ready! Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.strip().lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break

    response = llm.invoke(user_input)
    print("🦙 Ollama:", response.content)