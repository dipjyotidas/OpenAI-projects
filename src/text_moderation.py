# Open AI API
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')

# Create a request to the Moderation endpoint
response = openai.Moderation.create(
    model = "text-moderation-latest",
    input = "My favorite book is How to Kill a Mockingbird."
)

# Print the category scores
print(response["results"][0]["category_scores"])

# Sample output:

# {
#   "sexual": 9.011665724756313e-07,
#   "hate": 5.238259745965479e-07,
#   "harassment": 3.4255714126629755e-05,
#   "self-harm": 5.782478496030308e-09,
#   "sexual/minors": 5.687450155278384e-08,
#   "hate/threatening": 2.622775596705651e-08,
#   "violence/graphic": 8.806916866888059e-07,
#   "self-harm/intent": 9.663713163021725e-10,
#   "self-harm/instructions": 1.604589724979455e-11,
#   "harassment/threatening": 3.3559299481566995e-06,
#   "violence": 0.0500854030251503
# }