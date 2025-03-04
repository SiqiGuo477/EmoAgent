from flask import Flask, render_template, request
import openai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize Flask app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method == "POST":
        user_input = request.form["user_input"]
        client = openai.OpenAI(api_key=OPENAI_API_KEY)
        
        # Send user input to OpenAI
        openai_response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )
        
        # Extract response text
        response = openai_response.choices[0].message.content

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
