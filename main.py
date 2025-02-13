
api_key = "AIzaSyDNqMFbf1kCkx-7NJp61yQzjLA0VQ5Ixdc"
from flask import Flask, render_template, request
import google.generativeai as genai
import re

app = Flask(__name__)

# Set up the API key (Ensure it's correctly defined)

genai.configure(api_key=api_key)

def format_response(text):
    """Formats response: keeps line breaks and highlights text between ** ** in bold red."""
    text = text.replace("\n", "<br>")  # Preserve new lines
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color: red;">\1</strong>', text)  # Bold & red
    return text

@app.route("/", methods=["GET", "POST"])
def index():
    response_text = ""
    if request.method == "POST":
        user_input = request.form.get("user_input", "").strip()
        
        if user_input:
            model = genai.GenerativeModel("gemini-1.5-flash")
            response = model.generate_content(user_input)
            response_text = format_response(response.text) if response.text else "No response generated."

    return render_template("index.html", response_text=response_text)

if __name__ == "__main__":
    app.run(debug=True)
