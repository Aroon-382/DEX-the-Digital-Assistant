import ollama

def chat():
    print("=" * 40)
    print("   D.E.X The Digital Assistant - Powered by llama3.2")
    print("=" * 40)
    print("Hey there!👋 Im D.E.X, your digital assistant. Ask me anything about math, science, history. I'm here to help you with any questions you have. Let's get started!😁")
    print("Type 'exit' to stop the conversation!.\n")

    conversation_history = []

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("Ok! Goodbye!👋")
            break

        if not user_input:
            print("Please type something!\n")
            continue

        conversation_history.append({
            "role": "user",
            "content": user_input
        })

        print("Bot: ", end="", flush=True)
        full_response = ""

        for chunk in ollama.chat(
            model="llama3.2",
            messages=conversation_history,
            stream=True
        ):
            token = chunk["message"]["content"]
            print(token, end="", flush=True)
            full_response += token

        print("\n")

        conversation_history.append({
            "role": "assistant",
            "content": full_response
        })

if __name__ == "__main__":
    chat()