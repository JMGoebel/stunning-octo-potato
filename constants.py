import os
from groq import Groq
from dotenv import load_dotenv
from llama_index.embeddings.openai import OpenAIEmbedding, OpenAIEmbeddingModelType
from llama_index.llms.groq import Groq

load_dotenv()

# LLM
groq_api_key = os.getenv("GROQ_API_KEY")
llm_model = Groq(model="llama3-70b-8192" ,api_key=groq_api_key)

# Embeddings
openai_api_key = os.getenv("OPENAI_API_KEY")
embed_model = OpenAIEmbedding(model=OpenAIEmbeddingModelType.TEXT_EMBED_3_LARGE, api_key=openai_api_key)
