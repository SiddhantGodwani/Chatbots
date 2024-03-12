#Bard api using chatbot
#API -   bAg_kh7eaWMTw9tQR6baPxHiRm1FVf_5OPje4qN5rA7wccRceJWGOf6_fH0WmVkXMCfXOw.

from bardapi import Bard
import os
#import time
token='bAg_kh7eaWMTw9tQR6baPxHiRm1FVf_5OPje4qN5rA7wccRceJWGOf6_fH0WmVkXMCfXOw.'

# Replace XXXX with the values you get from __Secure-1PSID
os.environ['_BARD_API_KEY']="bAg_kh7eaWMTw9tQR6baPxHiRm1FVf_5OPje4qN5rA7wccRceJWGOf6_fH0WmVkXMCfXOw."


# Set your input text
# input_text = "Why is the sky blue?"
# input_text = "What is the current status of E waste in india"

message = input("You: ")
print(Bard().get_answer(str(message)))

# print(Bard().get_answer(input_text)['content'])