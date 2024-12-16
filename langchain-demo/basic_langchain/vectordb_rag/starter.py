from datasets import load_dataset
from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
# from DLAIUtils import Utils
# import DLAIUtils

import os
import time
import torch

dataset = load_dataset('quora', split='train[240000:290000]', trust_remote_code=True)
print(dataset[0])
print(load_dataset('squad', split='train')[0])

questions = []
for record in dataset['questions']:
    questions.extend(record['text'])
question = list(set(questions))
print('\n'.join(questions[:10]))
print('-' * 50)
print(f'Number of questions: {len(questions)}')

device = 'cuda' if torch.cuda.is_available() else 'cpu'
if device != 'cuda':
    print('Sorry no cuda.')
model = SentenceTransformer('all-MiniLM-L6-v2', device=device)

query = 'which city is the most populated in the world?'
xq = model.encode(query)
xq.shape