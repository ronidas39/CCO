from graph_builder import build_graph

if __name__ == "__main__":
    # For standalone mode, we simulate a continuous conversation.
    state = {"messages": []}
    while True:
        user_input = input("User: ")
        if user_input.lower() in ["quit", "exit", "q"]:
            print("Exiting conversation.")
            break
        state["messages"].append({"role": "user", "content": user_input})
        result = build_graph().invoke(state)
        # Update state with latest messages.
        state = result
        for msg in result.get("messages", []):
            if msg.get("role") == "assistant":
                print(f"Assistant: {msg['content']}")
