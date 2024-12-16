from transformers.utils import logging
from transformers import pipeline

logging.set_verbosity_error()

# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")
user_message= '''What is Apple?'''

pipe(user_message)
# from transformers import Conversation 

# conversation = Conversation(user_message)
# print(conversation)