from flask import Flask
from multiprocessing import Process
from botfunctions import startbot


app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello, World!'

def run_flask():
    app.run(debug=False, host='0.0.0.0', port=5000)

def run_bot():
    startbot.initializebot()

if __name__ == '__main__':
    flask_process = Process(target=run_flask)
    flask_process.start()

    run_bot()
