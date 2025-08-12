from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")

    try:
        # Using OpenRouter API with a free model
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": "Bearer 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",  # Replace this
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-4o-mini", # You can try others like "google/gemma-7b-it"
                "messages": [
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": user_input}
                ]
            }
        )
        if response.status_code == 200:
            data = response.json()
            reply = data["choices"][0]["message"]["content"]
            return jsonify({"response": reply})
        else:
            return jsonify({"response": f"Error: {response.status_code} - {response.text}"})

    except Exception as e:
        return jsonify({"response": f"Error: {str(e)}"})

if __name__ == "__main__":
    app.run(debug=True)