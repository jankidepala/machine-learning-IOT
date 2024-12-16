from transformers import pipeline

transcriber = pipeline(task="automatic-speech-recognition", model="openai/whisper-small")
result = transcriber(
    "../audion/mlk.flac")

print(result)


# # Use a pipeline as a high-level helper
# from transformers import pipeline

# messages = [
#     {"role": "user", "content": "Who are you?"},
# ]
# pipe = pipeline("text-generation", model="pentagoniac/SEMIKONG-8b-GPTQ")
# pipe(messages)