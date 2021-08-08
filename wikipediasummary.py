from flask import Flask
import wikipedia as wikipedia_module

app = Flask(__name__)

@app.route('/<data>/')
def wikipedia(data):
    summary = wikipedia_module.summary(data)
    return summary

app.run()
