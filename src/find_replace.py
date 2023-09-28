# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Find and Replace using Completion endpoint

prompt="""Replace automobile with ship and adjust phrase:
A automobile is a vehicle that is typically powered by an internal combustion engine or an electric motor. It has four wheels, 
and is designed to carry passengers and/or cargo on roads or highways. Automobiles have become a ubiquitous part of modern society, 
and are used for a wide variety of purposes, such as commuting, travel, and transportation of goods. Automobiles are often associated with freedom, independence, and mobility."""

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model = "gpt-3.5-turbo-instruct",
  prompt = prompt,
  max_tokens = 100
)

# Extract and print the response text
print(response['choices'][0]['text'])
