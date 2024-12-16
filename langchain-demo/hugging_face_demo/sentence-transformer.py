from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

sentences1 = ['The cat sits outside','A man is playing guitar','The movies are awesome']
embeddings1 = model.encode(sentences1, convert_to_tensor=True)
sentences2 = ['The dog plays in the garden','A woman watches TV','The new movie is so great']
embeddings2 = model.encode(sentences2, convert_to_tensor=True)
print(embeddings2)