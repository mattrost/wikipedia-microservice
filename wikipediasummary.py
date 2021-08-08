from flask import Flask
import wikipedia as wikipedia_module

app = Flask(__name__)

@app.route('/')
def welcome():
    welcome = wikipedia_module.summary('Wikipedia')
    return welcome

@app.route('/<data>/')
def wikipedia(data):
    try:
        summary = wikipedia_module.summary(data)
        return summary
    except:
        error = 'Wikipedia search had errors, please try another search query.'
        return error

app.run()
