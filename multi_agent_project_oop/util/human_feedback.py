def human_feedback(agent_name: str, agent_output: str) -> str:
    print(f"\n--- {agent_name} produced the following output ---")
    print(agent_output)
    feedback = input(f"Modify output for '{agent_name}' if needed (press Enter to accept): ")
    return feedback.strip() if feedback.strip() else agent_output
