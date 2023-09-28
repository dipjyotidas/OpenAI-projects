# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Open the audio.wav file
audio_file = open("mandarin-full.wav", "rb")

# Create a translation from the audio file
response = openai.Audio.translate("whisper-1", audio_file)

# Extract and print the translated text
print(response["text"])

# Translate from Non English to English language

# The World Bank said in its latest economic outlook report that the global economy is in a dangerous state. As interest rates rise, 
# consumer spending and corporate investment will slow down, economic activities will be impacted, and the vulnerability of low-income countries will be exposed.
# Global economic growth will be significantly slowed down, and the stability of the financial system will be threatened.

# Translating with prompts

audio_file = open("mandarin-full.wav", "rb")

# Write an appropriate prompt to help the model
prompt = "The audio relates to a recent World Bank report"

# Create a translation from the audio file
response = openai.Audio.translate("whisper-1", audio_file, prompt=prompt)

# Extract and print the translated text
print(response["text"])

# Translation response:

# The World Bank said in its latest economic outlook report that the global economy is in a dangerous state. 
# As interest rates rise, consumer spending and corporate investment will slow down, economic activities will be impacted, 
# and the vulnerability of low-income countries will be exposed. Global economic growth will be significantly slowed down,
# and the stability of the financial system will be threatened.