# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

messages = [{"role": "system", "content": "You are a helpful math tutor."}]
user_msgs = ["Explain what pi is.", "Summarize this in two bullet points."]

for q in user_msgs:
    print("User: ", q)
    
    # Create a dictionary for the user message from q and append to messages
    user_dict = {"role": "user", "content": q}
    messages.append(user_dict)
    
    # Create the API request
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100
    )
    
    # Convert the assistant's message to a dict and append to messages
    assistant_dict = dict(response["choices"][0]["message"])
    messages.append(assistant_dict)
    print("Assistant: ", response["choices"][0]["message"]["content"], "\n")
    
#Example Chatbot response:

# User:  Explain what pi is.
# Assistant:  Pi (π) is a mathematical constant that represents the ratio of a circle's circumference to its diameter. In simpler terms, pi is the number you get when you divide the distance around a circle by the distance across it. 
# It is an irrational number, meaning it cannot be expressed as a fraction and its decimal representation goes on forever without repeating.

# Pi is approximately equal to 3.14159, but it is infinitely long and has been calculated to millions and even billions of decimal places using computers.      

# User:  Summarize this in two bullet points.
# Assistant:  - Pi is the ratio of a circle's circumference to its diameter.
# - It is an irrational number, approximately equal to 3.14159, with an infinite and non-repeating decimal representation. 