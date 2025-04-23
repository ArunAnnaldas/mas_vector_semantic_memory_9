def log_interaction(agent, prompt, response, token_info):
    with open(f"logs/{agent}.log", "a") as f:
        f.write(f"\n--- {agent.upper()} ---\n")
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Response: {response}\n")
        f.write(f"Tokens Used: {token_info}\n")