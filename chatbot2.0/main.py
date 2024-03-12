from flask import Flask, request, render_template
import re
import long_responses as long

app = Flask(__name__)

class Chatbot:
    def __init__(self):
        self.keywords = {
            "hello": ["hello", "hi", "sup", "hey", "yo"],
            "how are you": ["how are you", "how's it going", "what's up"],
            "what can you do": ["what can you do", "what's your purpose", "what are you good at"],
        }
        self.responses = long.responses

    def get_response(self, user_input):
        """Returns a response to the user's input."""

        # Split the user's input into words.
        split_message = re.split(r'\s+|[,;!.-]\s*', user_input.lower())

        # Find the keyword that matches the user's input.
        best_match = None
        highest_prob = 0
        for keyword, words in self.keywords.items():
            prob = 0
            for word in words:
                if word in split_message:
                    prob += 1
            if prob > highest_prob:
                best_match = keyword
                highest_prob = prob

        # If no keyword is found, return a default response.
        if best_match is None:
            return "I'm not sure what you mean. Can you rephrase your question?"

        # Return the response for the matched keyword.
        return self.responses[best_match]


# Create a chatbot object.
chatbot = Chatbot()

@app.route("/", methods=["GET", "POST"])
def chatbot():
    # Get the user's input.
    user_input = request.args.get("query")

    # Generate a response to the user's input.
    response = chatbot.get_response(user_input)

    # Return the response to the user.
    return render_template("chatbot.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
