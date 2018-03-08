from flask import Flask
app = Flask(__name__)

@app.route('/<message>')
def reply(message):
    return 'Message %s' % message
