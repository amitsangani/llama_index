import os
os.environ["OPENAI_API_KEY"] = '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'

from llama_index import GPTSimpleVectorIndex, SimpleDirectoryReader
documents = SimpleDirectoryReader('data').load_data()
index = GPTSimpleVectorIndex.from_documents(documents)
