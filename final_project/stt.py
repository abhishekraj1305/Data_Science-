import whisper
# import json

model = whisper.load_model("large-v2")

result = model.transcribe(audio = "audios/15_Exercise 2： Good Morning Sir.mp3", 
                          language="hi",
                          task="translate",
                          word_timestamps = False)

print(result["text"])