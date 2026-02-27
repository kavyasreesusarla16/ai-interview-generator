from flask import Flask, render_template, request
from groq import Groq
import os

app = Flask(__name__)

# Load your Groq API Key
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        role = request.form.get("role")
        difficulty = request.form.get("difficulty")
        qtype = request.form.get("qtype")
        count = request.form.get("count")

        prompt = f"""
        Generate {count} interview questions for the job role {role}.
        Difficulty: {difficulty}.
        Type: {qtype}.
        Give answers also.
        Format it cleanly with proper numbering.
        """

        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        result_text = response.choices[0].message.content

        return render_template("result.html", result=result_text)

    return render_template("index.html")

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
