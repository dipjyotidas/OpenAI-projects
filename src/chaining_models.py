# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Open the audio.wav file
audio_file = open("arne-german-automotive-forecast.wav", "rb")

# Create a transcription request using audio_file
audio_response = openai.Audio.transcribe("whisper-1", audio_file)

# Create a request to the API to identify the language spoken
chat_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a languages specialist."},
    {"role": "user", "content": "Identify the language used in the following text: " + audio_response["text"]}
  ]
)
print(chat_response["choices"][0]["message"]["content"])

# Response:
# The language used in the text is German.

# Creating meeting summaries

# Open the example datacamp-q2-roadmap.mp3 file
audio_file = open("datacamp-q2-roadmap-short.mp3", "rb")

# Create a transcription request using audio_file
audio_response = openai.Audio.transcribe("whisper-1", audio_file)

# Create a request to the API to summarize the transcript into bullet points
chat_response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "List the courses that DataCamp will be making as bullet points." + audio_response["text"]}
  ],
  max_tokens=100
)
print(chat_response["choices"][0]["message"]["content"])