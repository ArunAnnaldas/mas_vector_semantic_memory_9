import tiktoken

def count_tokens(prompt, response, model_name="gpt-3.5-turbo"):
    enc = tiktoken.encoding_for_model(model_name)
    prompt_tokens = len(enc.encode(prompt))
    response_tokens = len(enc.encode(response))
    total = prompt_tokens + response_tokens
    return {
        "prompt_tokens": prompt_tokens,
        "response_tokens": response_tokens,
        "total_tokens": total
    }