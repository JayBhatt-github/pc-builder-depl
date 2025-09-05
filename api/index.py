from flask import Flask, jsonify
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({"message": "Hello from Flask on Vercel!"})

# For local testing
if __name__ == "__main__":
    app.run(debug=True)
