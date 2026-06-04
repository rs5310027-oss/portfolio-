from flask import Flask, render_template, request, jsonify
import nltk

app = Flask(__name__)

# Simple intent-response dictionary
responses = {
    "hello": "Hi there!",
    "how are you": "I'm doing great!",
    "bye": "Goodbye!",
    "help": "How can I help you?"
}

def get_response(user_input):
    user_input = user_input.lower()

    for intent in responses:
        if intent in user_input:
            return responses[intent]

    return "Sorry, I don't understand."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    bot_response = get_response(user_message)

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)