from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello from Azure! (Python 3.13)", 200

if __name__ == "__main__":
    # local dev server (not used in production on App Service)
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)))
