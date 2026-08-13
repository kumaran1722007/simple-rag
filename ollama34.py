import ollama
import time

LLM='qwen3.5:0.8b'

start = time.time()
resp = ollama.chat(model=LLM, messages=[{'role':'user','content':'hi'}],options={'num_ctx': 2048},
    keep_alive='30m')
print(f"took {time.time() - start:.1f}s")
print(resp['message']['content'])