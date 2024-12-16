from transformers import pipeline

# Load the pre-trained sentiment analysis model
sentiment_analysis = pipeline("automatic-speech-recognition", model="pentagoniac/SEMIKONG-8b-GPTQ")

input_text = [
    "World is a beautiful place with bad people"
]

# result = sentiment_analysis(input_text)
print(sentiment_analysis)