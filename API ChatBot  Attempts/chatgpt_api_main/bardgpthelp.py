from bardapi import Bard
import os

# Replace 'YOUR_API_KEY' with your actual Bard API key
api_key = 'bAg_kh7eaWMTw9tQR6baPxHiRm1FVf_5OPje4qN5rA7wccRceJWGOf6_fH0WmVkXMCfXOw.'

# Set the Bard API key as an environment variable
os.environ['_BARD_API_KEY'] = api_key

# Set your input text
input_text = "What is the current status of E waste in India?"

# Initialize Bard and get the answer
bard = Bard()
response = bard.get_answer(input_text)

# Print the response content
print(response['content'])
