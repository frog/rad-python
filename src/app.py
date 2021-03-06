from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello world!"

if __name__ == "__main__":
    app.run(
        debug=os.environ['FLASK_DEBUG'],
        host=os.environ['FLASK_HOST'],
        port=int(os.environ['FLASK_PORT'])
    )
