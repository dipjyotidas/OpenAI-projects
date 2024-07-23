# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Create a request to the Completion endpoint
response = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages =[
      {"role":"user",
       "content":"Generate a catchy slogan for fine dining continental restuarant"}
  ],
  max_tokens = 200
)

print(response.choices[0].message.content)

#response:"Savor the Taste of Elegance at Our Continental Paradise!"