import asyncio
import json
import os
from dotenv import load_dotenv  
from bardapi import Bard

load_dotenv()
BARD_API_KEY = os.getenv('key')

bardapi = Bard(token=BARD_API_KEY)

async def answer_question(question):
    
    response = await bardapi.query(question)
    return json.loads(response)['answer']

async def chatbot_loop():
    while True:
        question = input('> ')
        response = await answer_question(question)
        print(response)

if __name__ == '__main__':
    if asyncio.get_event_loop() is None:
        asyncio.run(chatbot_loop())
    else:
        chatbot_loop()
