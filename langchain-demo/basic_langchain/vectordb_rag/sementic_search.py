import os, time, torch, tqdm
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from sentence_transformers import SentenceTransformer
from DLAIUtils import Utils
import DLAIUtils
from tqdm.auto import tqdm
from pinecone_datasets import load_dataset, list_datasets

os.path.join = lambda *s: "/".join(s)
my_key1 = os.getenv("PINECONE_API_KEY")
print('My Key present is  ')
print(my_key1)


device = 'cuda' if torch.cuda.is_available() else 'cpu'
if device != 'cuda':
    print('Sorry no cuda.')
    
    #dataset
dataset = load_dataset('quora_all-MiniLM-L6-bm25')
# we drop metadata as will use blob column
dataset.documents.drop(['metadata'], axis=1, inplace=True)
dataset.documents.rename(columns={'blob': 'metadata'}, inplace=True)
# we will use 80K rows of the dataset between rows 240K -> 320K
dataset.documents.drop(dataset.documents.index[320_000:], inplace=True)
dataset.documents.drop(dataset.documents.index[:240_000], inplace=True)
dataset.head()
print(len(dataset))

index_name = "quickstart1"

pc = Pinecone('4fd90e81-6234-4076-bd1f-b23fb5f7feb2')
print('INDEX: ')
print(pc.list_indexes())
existing_indexes = [
    index_info["name"] for index_info in pc.list_indexes()
]
print(len(existing_indexes))

# print(pc.list_indexes().names)
if index_name not in existing_indexes:
    pc.create_index(
        name=index_name,
        dimension=2, # Replace with your model dimensions
        metric="cosine", # Replace with your model metric
        spec=ServerlessSpec(
            cloud="aws",
            region="us-east-1"
        ) 
    )
    # wait for index to be initialized
while not pc.describe_index(index_name).status['ready']:
    index = pc.Index(index_name)
    print(index)
    time.sleep(1)
    
# view index stats
index = pc.Index(index_name)
print('AAAAAAAAAAAAAAAA')
index.describe_index_stats()

index.upsert(
    vectors=[
        {
            "id": "vec1", 
            "values": [1.0, 1.5], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec2", 
            "values": [2.0, 1.0], 
            "metadata": {"genre": "action"}
        }, {
            "id": "vec3", 
            "values": [0.1, 0.3], 
            "metadata": {"genre": "drama"}
        }, {
            "id": "vec4", 
            "values": [1.0, -2.5], 
            "metadata": {"genre": "action"}
        }
    ],
    namespace= "ns1"
)
print('BBBBBBBBBBBBBBBBBB')
index.describe_index_stats()

response = index.query(
    namespace="ns1",
    vector=[0.1, 0.3],
    top_k=2,
    include_values=True,
    include_metadata=True,
    filter={"genre": {"$eq": "action"}}
)
    
print(response)

#Upsert the data
from tqdm.auto import tqdmc 

for batch in tqdm(dataset.iter_documents(batch_size=500), total=160):
    index.upsert(batch)

#Make queries
query = "which country has the highest population in the world?"

# create the query vector
xq = model.encode(query).tolist()

# now query
xc = index.query(vector=xq, top_k=5, include_metadata=True)

for result in xc['matches']:
    print(f"{round(result['score'], 2)}: {result['metadata']['text']}")
    
#Modify
query = "which metropolis has the highest number of people?"

# create the query vector
xq = model.encode(query).tolist()

# now query
xc = index.query(vector=xq, top_k=5, include_metadata=True)
for result in xc['matches']:
    print(f"{round(result['score'], 2)}: {result['metadata']['text']}")
    
# 0.36:  Which is the best book to learn Phyton?
# 0.36:  How does Guernica show cubism?
# 0.35:  How is Guernica an example of cubism?
# 0.35:  How do Pokémon reproduce?
# 0.34:  What is a Punnet square? What are some uses of Punnett squares?