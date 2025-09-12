# llm_client.py
import os
import requests

# Option A: Hugging Face Inference API
# Set your key: export HF_TOKEN="..."
HF_MODEL = "HuggingFaceH4/zephyr-7b-beta"
HF_API = f"https://api-inference.huggingface.co/models/{HF_MODEL}"
HF_HEADERS = {"Authorization": f"Bearer {os.getenv('HF_TOKEN')}"}

def call_hf_llm(prompt: str):
    resp = requests.post(
        HF_API,
        headers=HF_HEADERS,
        json={"inputs": prompt, "parameters": {"max_new_tokens": 300}}
    )
    if resp.status_code == 200:
        try:
            return resp.json()[0]["generated_text"]
        except Exception:
            return str(resp.json())
    return f"Error {resp.status_code}: {resp.text}"

# Option B: Local LLM (llama.cpp / vllm) can be added here

if __name__ == "__main__":
    test = call_hf_llm("Solve: If 2x+3=7, find x. Return JSON {answer:..., steps:...}")
    print(test)
