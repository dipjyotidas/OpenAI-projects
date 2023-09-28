# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt = "Generate a catchy slogan for fine dining French restaurant",
  max_tokens = 100
)

print(response["choices"][0]["text"])