from flask import Flask
import wikipedia as wikipedia_module

app = Flask(__name__)

@app.route('/')
def welcome():
    welcome = 'Hello! Please enter a wikipedia search after the `.com/` to search for a Wikipedia summary.'
    return welcome

@app.route('/<data>/')
def wikipedia(data):
    try:
        summary = wikipedia_module.summary(data)
        return summary
    except:
        error = 'Wikipedia search had errors, please try another search query.'
        return error

if __name__ == '__main__':
    app.run()
