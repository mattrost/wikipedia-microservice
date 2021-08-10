from flask import Flask
from flask_cors import CORS, cross_origin
import wikipedia as wikipedia_module

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-type'

@app.route('/')
@cross_origin()
def welcome():
   
    welcome = 'Hello! Please enter a wikipedia search after the `.com/` to search for a Wikipedia summary.'
    return welcome

@app.route('/<data>/')
@cross_origin()
def wikipedia(data):
    try:
        summary = wikipedia_module.summary(data)
        response = {
            'search': data,
            'summary': summary
        }
        return response
    except:
        error = 'Wikipedia search had errors, please try another search query.'
        return error

if __name__ == '__main__':
    app.run()
