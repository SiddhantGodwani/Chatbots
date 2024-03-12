import openai

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'YOUR_API_KEY'

# Initialize the OpenAI API client
openai.api_key = api_key

def ask_question(question):
    response = openai.Completion.create(
        engine="davinci",  # Use the 'davinci' engine
        prompt=question,
        max_tokens=50,  # You can adjust this value based on the desired response length
        stop=None  # You can specify stop words to limit the response
    )
    return response.choices[0].text.strip()

# Main chat loop
print("Chatbot: Hello! I'm here to answer your questions about e-waste.")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['bye', 'exit', 'quit']:
        print("Chatbot: Goodbye!")
        break
    response = ask_question(user_input)
    print("Chatbot:", response)
