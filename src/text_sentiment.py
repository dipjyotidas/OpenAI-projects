# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model="gpt-3.5-turbo-instruct",
  prompt= """
  classify the sentiment of the following statements as either negative, positive,  or neutral:
1. Unbelievably good!
2. Shoes fell apart on the second use.
3. The shoes look nice, but they aren't very comfortable.
4. Can't wait to show them off!
   """,
  max_tokens=100
)

print(response['choices'][0]['text'])