# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

prompt="""Summarize the following text into two concise bullet points:
Investment refers to the act of committing money or capital to an enterprise with the expectation of obtaining an added income or profit in return. 
There are a variety of investment options available, including stocks, bonds, mutual funds, real estate, precious metals, and currencies. 
Making an investment decision requires careful analysis, assessment of risk, and evaluation of potential rewards. Good investments have the ability 
to produce high returns over the long term while minimizing risk. Diversification of investment portfolios reduces risk exposure. Investment can be a 
valuable tool for building wealth, generating income, and achieving financial security. It is important to be diligent and informed when investing to avoid losses."""

# Create a request to the Completion endpoint
response = openai.Completion.create(
  model = "gpt-3.5-turbo-instruct",
  prompt = prompt,
  max_tokens = 400,
  temperature = 0
)
print(response["choices"][0]["text"])