api_key = "AIzaSyDNqMFbf1kCkx-7NJp61yQzjLA0VQ5Ixdc"
from flask import Flask, render_template, request
import google.generativeai as genai

app = Flask(__name__)

# Set up the API key
genai.configure(api_key=api_key)

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(user_input)
        response_text = response.text.replace("\n", "<br>")  # Keep formatting

    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
