from flask import Flask, request
from collections import namedtuple
app =  Flask(__name__)


@app.route('/')
def index():
    return'<h1>Home</h1>'

@app.route('/api')
def api():
    user_input = request.args.get('input')    #query name
    response = generate_response(user_input)
    
    json = {
        'input': user_input,
        'response': response.response,
        'accuracy': response.accuracy
    }
    
    return json


Response = namedtuple( 'Response', 'response accuracy')
def generate_response(user_input: str) -> Response:
    lc_input = user_input.Lower()
    
    if lc_input=="hello":
        return Response("Hey there")
    
    
    
    

    
if __name__ == '__main__':
    app.run()