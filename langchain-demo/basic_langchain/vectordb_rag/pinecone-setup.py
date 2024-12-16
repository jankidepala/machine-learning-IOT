import os 
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
from DLAIUtils import Utils
import DLAIUtils

my_key1 = os.getenv("PINECONE_API_KEY")
print('My Key present is  ')
print(my_key1)


utils = Utils()
PINECONE_API = utils.get_pinecone_api_key()
print(PINECONE_API)

# Unathorised
# pinecone = Pinecone(api_key=my_key1)
# print(pinecone.list_indexes())
INDEX_NAME = utils.create_dlai_index_name('dl-ai')
print(INDEX_NAME)

