from flask import Flask, jsonify
from flask_cors import CORS
from flask import request
from dictionaryGen import getFlagDictionary

app = Flask(__name__)
CORS(app)

@app.route("/members")

def members():
    return jsonify({
        "members": ["Member1", "Member2", "Member3"]
        })

@app.route("/submit-message", methods=["POST"])
def handle_message():
    data = request.json
    message = data.get("message", "")
    calculateResult(message)

    # Process the message here as needed
    return jsonify({"success": True, "message": "Received your message!"})


def calculateResult(text):
    flagDictionary = getFlagDictionary(text)
    #print(flagDictionary)


if __name__ == "__main__":
    app.run(debug=True)