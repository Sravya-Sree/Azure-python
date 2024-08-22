#my flask app
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World! from python flask app--Sravya"

if __name__ == "__main__":
    app.run(debug=True)