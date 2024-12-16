from transformers import pipeline

chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill", max_new_tokens=800)
user_message = "Name ten  fun activities I can do in the winter?"
input_text = "Can you convert this text to French language: Hello, How are you"
task="text2text-generation"
model_name = "google/flan-t5-base"
text2text_generator = pipeline(
    task,
    model = model_name)

print( text2text_generator(user_message) )