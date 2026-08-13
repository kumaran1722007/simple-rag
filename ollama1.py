from ollama import Client
import Rag

client=Client()

EB_model='hf.co/CompendiumLabs/bge-base-en-v1.5-gguf'
LLM='qwen3.5:0.8b'

topic='cat'

VECTOR_DB=[]

def add_chunks(chunks):
    embedding=client.embed(model=EB_model,input=chunks)['embeddings'][0]
    VECTOR_DB.append((chunks,embedding))
    
for i,chunks in enumerate(Rag.data):
    add_chunks(chunks)
    print(f"added {i+1}/{len(Rag.data)}to vector db")
print(VECTOR_DB[0])



def cosine_similarity(a, b):
  dot_product = sum([x * y for x, y in zip(a, b)])
  norm_a = sum([x ** 2 for x in a]) ** 0.5
  norm_b = sum([x ** 2 for x in b]) ** 0.5
  return dot_product / (norm_a * norm_b)



def retrive(query,top_n=1):
   query_embedding=client.embed(model=EB_model,input=query)['embeddings'][0]

   similarities=[]

   for chunks,embeddings in VECTOR_DB:
      similarity=cosine_similarity(query_embedding,embeddings)
      similarities.append((chunks,similarity))

   similarities.sort(key=lambda x:x[1],reverse=True)
   return similarities[:top_n]


input_q=input(f'ask me about {topic}:')
retrived_query=retrive(input_q)

for chunks,similarities in retrived_query:
   print(f'- (similarity :{similarities:.2f}) {chunks}')

instruction_prompt = f'''You are a helpful chatbot.
Use only the following pieces of context to answer the question. Don't make up any new information:
{'\n'.join([f' - {chunk}' for chunk, similarity in retrived_query])}
'''

stream1=client.chat(
   model=LLM,
   messages=[
      {
         
         'role':'system',
         'content':instruction_prompt

       },
       {
          'role':'user',
          'content':input_q
       },
   ],
   stream=True,
)

print("chat bot thinking....")

for chunk in stream1:
   print(chunk['message']['content'],end='',flush=True)

'''resp = ollama.chat(model=LLM, messages=[{'role':'user','content':'say hi'}])
print(resp['message']['content'])'''
   


