# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Open the openai-audio.mp3 file
audio_file = open("audio-logan-advocate-openai_example.mp3", "rb")

# Create a transcript from the audio file
response = openai.Audio.transcribe("whisper-1", audio_file)

# Extract and print the transcript text
print(response["text"])

# Transcribe response from Audio file:

# Hi there, Logan, thank you for joining us on the show today. Thanks for having me. I'm super excited about this. Brilliant.
# We're going to dive right in, and I think ChatGPT is maybe the most famous AI product that you have at OpenAI, but I'd just like to get an 
# verview of what all the other AIs that are available are. 
# So I think two and a half years ago, OpenAI released the API that we still have available today, which is essentially our giving people access 
# to these models. And for a lot of people, giving people access to the model that powers ChatGPT, which is our consumer-facing first-party application, 
# which essentially just, in very simple terms, puts a nice UI on top of what was already available through our API for the last two and a half years. 
# So it's sort of democratizing the access to this technology through our API. And if you want to just play around with it as an end user, we have ChatGPT 
# available to the world as well.

# Example for Transcribing a Portuguese audio file

# Open the openai-audio.mp3 file
audio_file = open("audio-portuguese_example.m4a", "rb")

# Create a transcript from the audio file
response = openai.Audio.transcribe("whisper-1", audio_file)

# Extract and print the transcript text
print(response["text"])

# Transcribe respone of the Portuguese file:

# Olá, o meu nome é Eduardo, sou CTO no Datacamp. Espero que esteja a gostar deste curso que o James e eu criamos para você. 
# Esta API permite enviar um áudio e trazer para inglês. O áudio original está em português.