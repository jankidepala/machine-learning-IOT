from transformers import pipeline

chatbot = pipeline(task="text2text-generation", model="facebook/blenderbot-400M-distill", max_new_tokens=800)
user_message = "Name ten  fun activities I can do in the winter?"
input_text = "Can you convert this text to French language: Hello, How are you"
task="text2text-generation"
model_name = "google/flan-t5-base"


text2text_generator = pipeline(
    input_text,
    model = model_name)

print( text2text_generator(user_message) )

#  ['audio-classification', 'automatic-speech-recognition', 'depth-estimation', 'document-question-answering', 'feature-extraction', 'fill-mask', 'image-classification', 'image-feature-extraction', 'image-segmentation', 'image-to-image', 'image-to-text', 'mask-generation', 'ner', 'object-detection', 'question-answering', 'sentiment-analysis', 'summarization', 'table-question-answering', 'text-classification', 'text-generation', 'text-to-audio', 'text-to-speech', 'text2text-generation', 'token-classification', 'translation', 'video-classification', 'visual-question-answering', 'vqa', 'zero-shot-audio-classification', 'zero-shot-classification', 'zero-shot-image-classification', 'zero-shot-object-detection', 'translation_XX_to_YY']"