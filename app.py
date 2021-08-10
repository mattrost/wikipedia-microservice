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
        output = "[{ 'search': '%s', 'summary': '%s' }]" % (data, summary)
        return output
    except:
        error = 'Search was not able to find a result'
        output = "[{ 'error': '%s'}]" % (error)
        return output

if __name__ == '__main__':
    app.run()
