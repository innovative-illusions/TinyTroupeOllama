from tinytroupe.providers.custom_provider import CustomProvider

# Other imports and code...

def initialize_provider(provider_name, api_key, base_url):
    if provider_name == "custom":
        return CustomProvider(api_key, base_url)
    elif provider_name == "openai":
        return OpenAIProvider(api_key)
    elif provider_name == "azure":
        return AzureProvider(api_key)
    else:
        raise ValueError(f"Unsupported provider: {provider_name}")

# Other functions and code...

def main():
    provider_name = "custom"  # or "openai" or "azure"
    api_key = "your_api_key"
    base_url = "http://192.168.1.151:1234"

    provider = initialize_provider(provider_name, api_key, base_url)

    model = "text-embedding-nomic-embed-text-v1.5"
    input_text = "Your input text here"
    embeddings = provider.get_embeddings(model, input_text)
    print(embeddings)

    model = "minicpm-v-2_6"
    prompt = "Your prompt here"
    completions = provider.get_completions(model, prompt)
    print(completions)

if __name__ == "__main__":
    main()
