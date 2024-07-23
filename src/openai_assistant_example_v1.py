# OpenAI Assistant
import openai
# Set your API key : https://platform.openai.com/account/api-keys
# store the API key in Environment variable : https://networkdirection.net/python/resources/env-variable/
import os
openai.api_key = os.environ.get('OpenAI_API_Key')
from openai import OpenAI
client = OpenAI(api_key=openai.api_key)

# In this example, we’ll create an assistant that can help answer questions about a scientific paper.

#Step 1: Create a new Assistant with File Search Enabled

assistant = client.beta.assistants.create(
  name="Scientific Paper Assistant",
  instructions="You are a polite and expert knowledge retrieval assistant. Use the documents provided as a knowledge base to answer questions",
  model="gpt-4o",
  tools=[{"type": "file_search"}],
)
#print(assistant)

#Step 2: Upload files and add them to a Vector Store

# Create a vector store caled "Scientific Paper"
vector_store = client.beta.vector_stores.create(name="Scientific Paper")
 
# Ready the files for upload to OpenAI
# Path to the file to upload: 
file_paths = ["./data/NIPS-2017-attention-is-all-you-need-Paper.pdf"]
file_streams = [open(path, "rb") for path in file_paths]

# Use the upload and poll SDK helper to upload the files, add them to the vector store,
# and poll the status of the file batch for completion.
file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
  vector_store_id=vector_store.id, files=file_streams
)
 
# We can print the status and the file counts of the batch to see the result of this operation.
print(file_batch.status)
print(file_batch.file_counts)

# Step 3: Update the assistant to to use the new Vector Store
assistant = client.beta.assistants.update(
  assistant_id=assistant.id,
  tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
)

#Step 4: Create a thread
# Upload the user provided file to OpenAI
message_file = client.files.create(
  file=open("./data/NIPS-2017-attention-is-all-you-need-Paper.pdf", "rb"), purpose="assistants"
)
 
# Create a thread and attach the file to the message
thread = client.beta.threads.create(
  messages=[
    {
      "role": "user",
      "content": "Why do authors use the self-attention strategy in the paper?",
      # Attach the new file to the message.
      "attachments": [
        { "file_id": message_file.id, "tools": [{"type": "file_search"}] }
      ],
    }
  ]
)
 
# The thread now has a vector store with that file in its tool resources.
print(thread.tool_resources.file_search)

# Use the create and poll SDK helper to create a run and poll the status of
# the run until it's in a terminal state.

run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id, assistant_id=assistant.id
)

messages = list(client.beta.threads.messages.list(thread_id=thread.id, run_id=run.id))

message_content = messages[0].content[0].text
annotations = message_content.annotations
citations = []
for index, annotation in enumerate(annotations):
    message_content.value = message_content.value.replace(annotation.text, f"[{index}]")
    if file_citation := getattr(annotation, "file_citation", None):
        cited_file = client.files.retrieve(file_citation.file_id)
        citations.append(f"[{index}] {cited_file.filename}")

print(message_content.value)
print("\n".join(citations))
    