from llama_cpp import Llama

llm = Llama(
      model_path="./models/mistral-7b-instruct-v0.2.Q4_0.gguf",
      n_gpu_layers=-1,
      seed=1337,
      n_ctx=2048,
)

def chat_query(query):
    response = llm.create_chat_completion(
    messages=[
        {
            "role": "user",
            "content": query
        }
    ]
    )
    return response['choices'][0]['message']['content']
